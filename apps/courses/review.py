"""What a teacher should verify in a lesson: the sentences the writers flagged, and a fingerprint of the content.

The writers marked facts that textbooks differ on, or that they could not confirm, with phrases such as
"check your textbook", "check your copy" or "check the current rules". The review checklist document and
the studio's review queue both find those sentences here, so they always agree.
"""

import hashlib
import json
import re

NOTE = re.compile(
    r"check (?:your (?:textbook|copy|tables|text)|the current (?:rules|position|figures|Finance Law)|current (?:rules|figures)"
    r"|with your teacher|the Finance Law|your school)", re.I)
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(“\"'])")


def block_texts(body="", title="", data=None):
    """Every piece of student-facing text in one block."""
    pieces = [body or "", title or ""]
    for value in (data or {}).values():
        if isinstance(value, str):
            pieces.append(value)
        elif isinstance(value, list):
            pieces += [v for v in value if isinstance(v, str)]
    return pieces


def flagged_in(pieces):
    """The flagged sentences in some text, in order, without repeats (each cut to 320 characters)."""
    found = []
    for piece in pieces:
        for sentence in SENTENCE.split(" ".join(piece.split())):
            if NOTE.search(sentence) and sentence[:320] not in found:
                found.append(sentence[:320])
    return found


def sentence_key(sentence):
    """A short stable id for a flagged sentence, used to remember which ones a reviewer ticked."""
    return hashlib.sha1(sentence.encode("utf-8")).hexdigest()[:12]


def lesson_flags(blocks):
    """Flagged sentences of a lesson's blocks: [{"key", "sentence", "block" (1-based position), "anchor"}]."""
    flags, seen = [], set()
    for number, block in enumerate(blocks, start=1):
        for sentence in flagged_in(block_texts(block.body, block.title, block.data)):
            key = sentence_key(sentence)
            if key not in seen:
                seen.add(key)
                flags.append({"key": key, "sentence": sentence, "block": number, "anchor": f"b{number}"})
    return flags


def fingerprint(blocks):
    """A hash of everything students see in a lesson's blocks: it changes whenever the content does."""
    content = [(b.block_type, b.title, b.body, b.media_url, b.alt_text, b.data) for b in blocks]
    return hashlib.sha1(json.dumps(content, sort_keys=True, default=str).encode("utf-8")).hexdigest()
