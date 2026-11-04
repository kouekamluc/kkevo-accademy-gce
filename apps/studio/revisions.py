"""Safe editing of lessons: working copies, snapshots, restore and the audit log.

Rule: a lesson that is *published* is never edited in place. The first block edit creates a
`LessonDraft` (a JSON copy of the live blocks) and the studio edits that copy. Publishing the
draft writes it back onto the live `LessonBlock` rows, updating rows in place so their ids stay
stable. Lessons that are not published (draft, review, archived) are invisible to students and are
edited directly. A draft only exists while its lesson is published: when a lesson leaves the
published state, its draft is folded into the (now hidden) live blocks.
"""

import copy

from django.db import transaction
from django.db.models import Max

from apps.courses.models import LessonBlock

from .models import LessonDraft, LessonEvent, LessonRevision

BLOCK_FIELDS = ("block_type", "title", "body", "media_url", "alt_text", "data")


def serialize(block):
    item = {field: copy.deepcopy(getattr(block, field)) for field in BLOCK_FIELDS}
    item["id"] = block.pk
    item["source"] = block.pk
    return item


def live_items(lesson):
    return [serialize(b) for b in LessonBlock.objects.filter(lesson=lesson).order_by("order", "pk")]


def to_block(lesson, item, order):
    """An unsaved LessonBlock for rendering and validating a JSON item (pk = item id)."""
    block = LessonBlock(lesson=lesson, order=order, **{f: copy.deepcopy(item.get(f, "" if f != "data" else {}))
                                                      for f in BLOCK_FIELDS})
    block.pk = item["id"]
    return block


def get_draft(lesson):
    return LessonDraft.objects.filter(lesson=lesson).first()


def start_draft(lesson, user):
    """Return the lesson's working copy, creating it from the live blocks if needed."""
    draft = get_draft(lesson)
    if draft:
        return draft
    items = live_items(lesson)
    top = LessonBlock.objects.filter(lesson=lesson).aggregate(m=Max("pk"))["m"] or 0
    draft = LessonDraft.objects.create(lesson=lesson, blocks=items, next_id=top + 1, created_by=user)
    log(lesson, user, LessonEvent.Action.CHANGES_STARTED)
    return draft


def write_live(lesson, items):
    """Make the live blocks match `items`, updating rows whose id is the item's `source`."""
    live = {b.pk: b for b in LessonBlock.objects.filter(lesson=lesson)}
    kept = set()
    with transaction.atomic():
        for order, item in enumerate(items, 1):
            values = {f: copy.deepcopy(item.get(f, "" if f != "data" else {})) for f in BLOCK_FIELDS}
            source = item.get("source")
            if source in live and source not in kept:
                block = live[source]
                for field, value in values.items():
                    setattr(block, field, value)
                block.order = order
                block.save()
                kept.add(source)
            else:
                LessonBlock.objects.create(lesson=lesson, order=order, **values)
        LessonBlock.objects.filter(lesson=lesson).exclude(pk__in=kept).filter(pk__in=list(live)).delete()


def snapshot(lesson, kind, user, items=None, note=""):
    number = (lesson.studio_revisions.aggregate(m=Max("number"))["m"] or 0) + 1
    return LessonRevision.objects.create(lesson=lesson, number=number, kind=kind, created_by=user, note=note[:300],
                                         blocks=live_items(lesson) if items is None else copy.deepcopy(items))


def log(lesson, user, action, comment="", from_status="", to_status="", revision=None):
    return LessonEvent.objects.create(lesson=lesson, actor=user, action=action, comment=comment.strip(),
                                      from_status=from_status, to_status=to_status, revision=revision)


def fold_draft(lesson):
    """Write a pending draft onto the live blocks and delete it. Returns True if there was one."""
    draft = get_draft(lesson)
    if not draft:
        return False
    write_live(lesson, draft.blocks)
    draft.delete()
    return True


def changes(draft, lesson):
    """Mark which draft items differ from the live lesson: ({item id: 'new'|'changed'}, removed count)."""
    live = {item["id"]: item for item in live_items(lesson)}
    marks, seen = {}, set()
    for item in draft.blocks:
        source = live.get(item.get("source"))
        if source is None:
            marks[item["id"]] = "new"
        else:
            seen.add(source["id"])
            if any(item.get(f) != source.get(f) for f in BLOCK_FIELDS):
                marks[item["id"]] = "changed"
    order_changed = [i.get("source") for i in draft.blocks if i.get("source") in live] != [k for k in live if k in seen]
    return marks, len(set(live) - seen), order_changed


def restore(lesson, revision, user):
    """Bring back a snapshot. Published lessons get it as draft changes (so it goes through review)."""
    live_ids = set(LessonBlock.objects.filter(lesson=lesson).values_list("pk", flat=True))
    if lesson.status == "published" or get_draft(lesson):
        draft = start_draft(lesson, user)
        items, used = [], set()
        for item in copy.deepcopy(revision.blocks):
            source = item.get("source")
            if source in live_ids and source not in used:
                item["id"] = source
                used.add(source)
            else:
                item["source"] = None
                item["id"] = draft.next_id
                draft.next_id += 1
            items.append(item)
        draft.blocks = items
        draft.status = LessonDraft.Status.DRAFT
        draft.save()
    else:
        snapshot(lesson, LessonRevision.Kind.BACKUP, user, note=f"Before restoring revision {revision.number}")
        write_live(lesson, [{**item, "source": item.get("source") if item.get("source") in live_ids else None}
                            for item in revision.blocks])
    lesson.save(update_fields=["updated_at"])
    log(lesson, user, LessonEvent.Action.RESTORED, comment=f"Restored revision {revision.number}.", revision=revision)
