"""Search across subjects, lessons, practice sets and mock exams.

The library is small enough (a few thousand titles) to rank in memory, which gives full control over what
"relevant" means for a GCE student: a word in a lesson title beats the same word in a summary, the student's
own class comes first, typing half a word already finds things, and a spelling slip still lands on the lesson.

The index is built once per process and rebuilt when the published content changes.
"""

import bisect
import math
import re
import threading
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from difflib import get_close_matches

from django.db.models import Count, Max
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from apps.core.models import PublicationStatus
from apps.practice.models import PracticeSet

from .models import Course, Lesson

SUBJECT, LESSON, PRACTICE, MOCK = "subject", "lesson", "practice", "mock"
KINDS = [(SUBJECT, "Subjects"), (LESSON, "Lessons"), (PRACTICE, "Practice"), (MOCK, "Mock exams")]

# How much a word counts depending on where it was found.
W_TITLE, W_CONCEPT, W_TOPIC, W_SUBJECT, W_TEXT = 10.0, 4.0, 4.0, 3.0, 2.0
EXACT, PREFIX, FUZZY = 1.0, 0.8, 0.55

STOPWORDS = frozenset(
    "a an and are as at be by for from how i in is it my of on or the to what when which with do does".split())

# What students actually type. Applied to the query before it is split into words.
PHRASES = [
    (r"\b(o|ordinary)[\s-]*levels?\b", " olevel "), (r"\b(a|advanced)[\s-]*levels?\b", " alevel "),
    (r"\bform\s*(5|five|v)\b|\bf5\b", " form5 "),
    (r"\b(lower\s*(sixth|6)|l6|lss)\b", " lowersixth "), (r"\b(upper\s*(sixth|6)|u6|uss)\b", " uppersixth "),
    (r"\bpast\s+(papers?|questions?)\b", " mock "), (r"\bcomputer\s+sci\b", " computer science "),
]
LEVEL_WORDS = {"olevel": {"form-5"}, "form5": {"form-5"}, "alevel": {"lower-sixth", "upper-sixth"},
               "lowersixth": {"lower-sixth"}, "uppersixth": {"upper-sixth"}}
SYNONYMS = {
    "math": "mathematics", "maths": "mathematics", "mathematic": "mathematics", "bio": "biology",
    "chem": "chemistry", "phy": "physics", "phys": "physics", "eco": "economics", "econs": "economics",
    "econ": "economics", "geo": "geography", "lit": "literature", "cs": "computer", "comp": "computer",
    "fmaths": "further", "accounts": "accounting", "religion": "religious", "philo": "philosophy",
    "mocks": "mock",
}
KIND_WORDS = {"mock": MOCK}


def _fold(text):
    """Lower-case, strip accents, keep letters and digits."""
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def _stem(word):
    """Light plural stripping, so 'forces' finds 'force' and 'theories' finds 'theory'."""
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def _words(text):
    return [_stem(w) for w in _fold(text).split()]


@dataclass
class Doc:
    kind: str
    pk: int
    title: str
    url: str
    subject: object
    level_slug: str
    level_name: str
    offering_id: int
    crumb: str = ""
    detail: str = ""
    order: tuple = ()
    folded_title: str = ""


@dataclass
class Hit:
    doc: Doc
    score: float
    title_html: str = ""

    def __getattr__(self, name):  # templates read hit.title, hit.url, ... straight from the document
        return getattr(self.doc, name)


@dataclass
class Index:
    signature: tuple
    docs: list = field(default_factory=list)
    postings: dict = field(default_factory=dict)   # stem -> {doc number: best field weight}
    vocabulary: list = field(default_factory=list)  # sorted stems, for prefix and fuzzy lookups
    surface: dict = field(default_factory=dict)     # stem -> the spelling to show ("photosynthesis")


_index = None
_lock = threading.Lock()


def _signature():
    lessons = Lesson.objects.filter(status=PublicationStatus.PUBLISHED).aggregate(n=Count("pk"), t=Max("updated_at"))
    sets = PracticeSet.objects.filter(status=PublicationStatus.PUBLISHED).aggregate(n=Count("pk"), t=Max("updated_at"))
    courses = Course.objects.published().aggregate(n=Count("pk"), t=Max("updated_at"))
    return tuple(v for row in (lessons, sets, courses) for v in (row["n"], row["t"]))


def get_index():
    global _index
    signature = _signature()
    if _index is None or _index.signature != signature:
        with _lock:
            if _index is None or _index.signature != signature:
                _index = _build(signature)
    return _index


def reset_index():
    global _index
    _index = None


def _build(signature):
    index = Index(signature=signature)
    postings = defaultdict(dict)
    spellings = defaultdict(Counter)

    def add(doc, fields):
        number = len(index.docs)
        doc.folded_title = _fold(doc.title)
        index.docs.append(doc)
        for weight, text in fields:
            for raw in _fold(text).split():
                stem = _stem(raw)
                if postings[stem].get(number, 0) < weight:
                    postings[stem][number] = weight
                spellings[stem][raw] += 1

    courses = (Course.objects.published()
               .select_related("offering__subject", "offering__level").order_by("offering__subject__order", "pk"))
    course_by_pk = {}
    for course in courses:
        subject, level = course.offering.subject, course.offering.level
        course_by_pk[course.pk] = course
        aliases = " ".join(filter(None, [subject.slug.replace("-", " "), subject.icon_text if subject.icon_text.isalpha() else ""]))
        add(Doc(SUBJECT, course.pk, subject.name, course.get_absolute_url(), subject, level.slug, level.name,
                course.offering_id, crumb=level.name, detail=course.summary, order=(subject.order, level.pk)),
            # Names only: a subject card should answer "chemistry", not every word in its description.
            [(W_TITLE, subject.name), (W_TITLE, aliases)])

    lessons = (Lesson.objects.filter(status=PublicationStatus.PUBLISHED, topic__module__course__in=course_by_pk)
               .values("pk", "title", "summary", "key_concepts", "estimated_minutes", "order", "topic__title",
                       "topic__order", "topic__module__title", "topic__module__order", "topic__module__course"))
    for row in lessons:
        course = course_by_pk[row["topic__module__course"]]
        subject, level = course.offering.subject, course.offering.level
        add(Doc(LESSON, row["pk"], row["title"],
                reverse("courses:lesson", kwargs={"course_slug": course.slug, "pk": row["pk"]}),
                subject, level.slug, level.name, course.offering_id,
                crumb=f"{subject.name} · {level.name} · {row['topic__module__title']}",
                detail=f"{row['estimated_minutes']} min lesson",
                order=(subject.order, level.pk, row["topic__module__order"], row["topic__order"], row["order"])),
            [(W_TITLE, row["title"]), (W_CONCEPT, row["key_concepts"]), (W_TOPIC, row["topic__title"]),
             (W_TOPIC, row["topic__module__title"]), (W_SUBJECT, subject.name), (W_TEXT, row["summary"])])

    sets = (PracticeSet.objects.filter(status=PublicationStatus.PUBLISHED, topic__module__course__in=course_by_pk)
            .annotate(n=Count("questions"))
            .values("pk", "title", "is_mock", "time_limit_minutes", "n", "order", "topic__title", "topic__order",
                    "topic__module__title", "topic__module__order", "topic__module__course"))
    for row in sets:
        course = course_by_pk[row["topic__module__course"]]
        subject, level = course.offering.subject, course.offering.level
        mock = row["is_mock"]
        detail = f"{row['n']} questions" + (f" · {row['time_limit_minutes']} min" if mock and row["time_limit_minutes"] else "")
        add(Doc(MOCK if mock else PRACTICE, row["pk"], row["title"], reverse("practice:set", kwargs={"pk": row["pk"]}),
                subject, level.slug, level.name, course.offering_id,
                crumb=f"{subject.name} · {level.name}" + ("" if mock else f" · {row['topic__title']}"), detail=detail,
                order=(subject.order, level.pk, row["topic__module__order"], row["topic__order"], row["order"])),
            [(W_TITLE, row["title"]), (W_TOPIC, row["topic__title"]), (W_TOPIC, row["topic__module__title"]),
             (W_SUBJECT, subject.name), (W_TEXT, "mock exam paper" if mock else "practice questions")])

    index.postings = dict(postings)
    index.vocabulary = sorted(postings)
    index.surface = {stem: forms.most_common(1)[0][0] for stem, forms in spellings.items()}
    return index


@dataclass
class Query:
    text: str
    terms: list = field(default_factory=list)   # stems the content must contain
    levels: set = field(default_factory=set)    # class named in the query ("o level", "upper sixth")
    kind: str = ""                               # "mock" or "practice" named in the query


def parse(text):
    query = Query(text=text)
    folded = " " + _fold(text) + " "
    for pattern, replacement in PHRASES:
        folded = re.sub(pattern, replacement, folded)
    words = []
    for raw in folded.split():
        if raw in LEVEL_WORDS:
            query.levels |= LEVEL_WORDS[raw]
            continue
        raw = SYNONYMS.get(raw, raw)
        if raw in KIND_WORDS:
            query.kind = KIND_WORDS[raw]
            continue
        words.append(_stem(raw))
    meaningful = [w for w in words if w not in STOPWORDS]
    query.terms = list(dict.fromkeys(meaningful or words))
    return query


def _expand(index, term, allow_prefix, allow_fuzzy):
    """Vocabulary words a query term can stand for, each with how good the match is."""
    found = {}
    if term in index.postings:
        found[term] = EXACT
    if not found and allow_prefix and len(term) >= 2:  # a whole word wins; half a word finds what it starts
        start = bisect.bisect_left(index.vocabulary, term)
        for word in index.vocabulary[start:start + 60]:
            if not word.startswith(term):
                break
            found.setdefault(word, PREFIX)
    if not found and allow_fuzzy and len(term) >= 4:
        near = [w for w in index.vocabulary if abs(len(w) - len(term)) <= 2 and not w.isdigit()]
        same_start = [w for w in near if w[0] == term[0]]
        for word in get_close_matches(term, same_start, n=3, cutoff=0.78) or get_close_matches(term, near, n=2, cutoff=0.82):
            found[word] = FUZZY
    return found


def search(text, *, user_level=None, enrolled=(), level=None, kind=None):
    """Rank the library against a query.

    Returns a dict: hits (best first), counts per kind, corrected (the spelling used when a word was not
    found as typed), and the levels the query itself named.
    """
    index = get_index()
    query = parse(text)
    result = {"hits": [], "counts": {k: 0 for k, _ in KINDS}, "corrected": "", "query": query}
    levels = {level} if level else query.levels
    wanted_kind = kind or query.kind
    if not query.terms:
        if not (query.levels or query.kind):
            return result
        # "o level mock exams": no topic words, so list that kind for that class.
        scores = {n: 1.0 for n, d in enumerate(index.docs)
                  if (not levels or d.level_slug in levels) and (not query.kind or d.kind == query.kind)}
        return _finish(index, query, scores, {}, result, user_level, enrolled, wanted_kind, levels)

    expansions, corrections = [], {}
    for position, term in enumerate(query.terms):
        last = position == len(query.terms) - 1
        words = _expand(index, term, allow_prefix=True, allow_fuzzy=True)
        if not last:  # a finished word should match as a word first; fall back to prefix only if it must
            exact = {w: q for w, q in words.items() if q != PREFIX}
            words = exact or words
        if words and all(q == FUZZY for q in words.values()):
            corrections[term] = index.surface.get(next(iter(words)), next(iter(words)))
        expansions.append(words)

    total = len(index.docs)

    def rarity(word):
        """Between 0.3 and 1: a word found in a handful of titles says more than one found in a whole subject."""
        return min(1.0, max(0.3, math.log(total / len(index.postings[word])) / math.log(max(total / 10, 2))))

    def score_all(required):
        scores, matched = defaultdict(float), defaultdict(int)
        for words in expansions:
            best = {}
            for word, quality in words.items():
                weigh = quality * rarity(word)
                for number, weight in index.postings[word].items():
                    value = weight * weigh
                    if best.get(number, 0) < value:
                        best[number] = value
            for number, value in best.items():
                scores[number] += value
                matched[number] += 1
        return {n: s for n, s in scores.items() if matched[n] >= required}

    scores = score_all(len(expansions))
    if not scores and len(expansions) > 1:  # nothing has every word: accept most of them
        scores = score_all(max(1, (len(expansions) + 1) // 2))
    if corrections:
        result["corrected"] = " ".join(corrections.get(_stem(SYNONYMS.get(w, w)), w) for w in _fold(text).split())
    return _finish(index, query, scores, expansions, result, user_level, enrolled, wanted_kind, levels)


def _finish(index, query, scores, expansions, result, user_level, enrolled, wanted_kind, levels):
    phrase = " ".join(_fold(query.text).split())
    highlight = sorted({w for words in expansions for w in words} if expansions else set(), key=len, reverse=True)
    hits = []
    for number, score in scores.items():
        doc = index.docs[number]
        if levels and doc.level_slug not in levels:
            continue
        if phrase and phrase in doc.folded_title:
            score += 6 + (4 if doc.folded_title.startswith(phrase) else 0)
        if doc.kind == SUBJECT:
            score += 5
        if query.kind and doc.kind == query.kind:
            score += 5
        if user_level and doc.level_slug == user_level:
            score += 3
        if doc.offering_id in enrolled:
            score += 1.5
        hits.append(Hit(doc, score))
    for kind_key, _ in KINDS:
        result["counts"][kind_key] = sum(1 for h in hits if h.doc.kind == kind_key)
    if wanted_kind:
        hits = [h for h in hits if h.doc.kind == wanted_kind]
    hits.sort(key=lambda h: (-round(h.score, 2), h.doc.order, h.doc.title))
    for hit in hits[:120]:
        hit.title_html = _highlight(hit.doc.title, highlight)
    result["hits"] = hits
    return result


def _highlight(title, stems):
    """The title as safe HTML with the matched words wrapped in <mark>."""
    if not stems:
        return escape(title)
    out = []
    for piece in re.split(r"(\w+)", title):
        if piece and piece[0].isalnum() and _stem(_fold(piece)) in stems:
            out.append(f"<mark>{escape(piece)}</mark>")
        else:
            out.append(escape(piece))
    return mark_safe("".join(out))
