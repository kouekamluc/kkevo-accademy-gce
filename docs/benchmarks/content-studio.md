# Benchmark: content authoring & administration

How established tools handle authoring, drafts vs published versions, review, media and audit
trails — and what the GCE Learning Academy studio (`/studio/`) takes from each. Based on the
public behaviour of each product, not on internal documentation.

## What they do

| Tool | Authoring | Draft vs published | Review / approval | Media | Audit trail |
|---|---|---|---|---|---|
| **Notion** | Typed blocks, slash menu, drag to reorder, autosave | No separate published copy: edits are live on shared pages | Comments and suggested edits on any block | Uploads inline into a block; no shared library | Page history with restore (length depends on plan) |
| **WordPress / Gutenberg** | Typed blocks with a sidebar for settings | Statuses draft / pending / published; with *revisions*, every save is a snapshot. Plain WordPress edits to a published post go live when you press Update; editorial plugins add "staged changes" | "Pending review" plus the `publish_posts` capability; plugins add editorial comments | Central media library: upload once, alt text, search, insert into an image block | Revisions screen: compare two versions, restore one |
| **Moodle** | Activities and resources inside course sections, edited in forms | Visible / hidden per activity, no staged copy | Not built in (workflow comes from plugins) | Per-course file areas with a file picker; repository plugins | Event logs: who did what and when, filterable by course or user |
| **Teachable / Thinkific** | Lectures built from content blocks in a course builder | Draft / published per lecture; edits to published lectures go live | None: one owner publishes | Video library with upload-and-reuse | Very little |
| **Khan Academy (internal tools, from public talks)** | Structured exercise and article editors | Content is edited in a draft and goes live only when it is *published*; students never see work in progress | Review and QA before publishing, comments kept beside the content | Shared, reusable image assets | Published revisions are kept and can be rolled back |

## What works well

1. **Students never see half-finished edits** (Khan Academy, WordPress "staged changes"). This
   matters for us because a broken worked example in a live revision lesson costs a student time
   they don't have before the exam.
2. **Revision snapshots with one-click restore** (WordPress, Notion). They make editing safe without
   anyone having to be careful.
3. **One media library, reused everywhere, with alt text at upload time** (WordPress). On slow
   connections an image is uploaded once and reused, and accessibility is enforced at the source.
4. **The review conversation stays next to the content** (Notion comments, Khan Academy review
   notes). A rejection without a reason sends the author guessing.
5. **An event log of who changed status and when** (Moodle logs, WordPress revisions authors).
6. **An overview of the work waiting for you** (WordPress dashboard, Moodle "recent activity").

## What we adopt

| Feature | From | How it works here |
|---|---|---|
| Draft changes to a published lesson | Khan Academy, WordPress staged changes | The first block edit on a published lesson creates a working copy (`studio.LessonDraft`, blocks stored as JSON). Students keep seeing the live blocks until a reviewer presses *Publish changes*. Live block rows are updated in place, so block ids (anchors, progress) stay the same. |
| Revision history + restore | WordPress revisions, Notion page history | A `LessonRevision` snapshot of all blocks (who, when, why) is saved on every submit and every publish, and before a restore. A restore goes into the working copy (and so through review) when the lesson is published, or into the blocks directly when it isn't. |
| Media library | WordPress | `studio.MediaAsset`: PNG/JPEG/GIF/WebP checked by content (not only by extension), size limit, stored under `MEDIA_ROOT/studio/`, alt text required. Search by title or alt text, and "Choose from library" in image blocks. |
| Review comments | Notion comments, Khan Academy review notes | An optional comment with every workflow action (submit, approve, send back). Comments appear in the editor's *Review notes* panel. |
| Audit log | Moodle event logs | A `LessonEvent` row for every status change, submission, publish, send-back, discard and restore, including bulk actions. Shown on the lesson history page and in the admin (read-only). |
| Studio overview | WordPress dashboard | `/studio/overview/`: counts by status, review queue (new lessons and changes to published lessons), my drafts, recent activity. |
| Curriculum tagging in the editor | Moodle competencies (lightweight) | Lesson settings list only the curriculum references of the lesson's own subject offering. Nothing official is invented: the list is empty until staff enter a syllabus. |

## What we skip, and why

- **Real-time co-editing and autosave on every keystroke (Notion).** Needs websockets, and
  autosaving often is costly on unreliable mobile data. Block-level saves are enough for 2–3 editors.
- **Visual side-by-side diff of two revisions (WordPress).** Instead the editor marks each block
  *New* or *Changed* and counts removed blocks, which covers most of a reviewer's need. A full diff can
  come later.
- **Video hosting library (Teachable/Thinkific).** Video is expensive to store and stream. Video blocks
  keep linking to external hosts.
- **SVG uploads.** SVG can carry scripts. Diagrams can be exported as PNG or WebP.
- **Inline suggestions or tracked changes (Notion, Google Docs).** A comment per review action is
  simpler and fits a small team.
- **Plugin or repository integrations (Moodle).** Out of scope for one platform.

## Known limits

- Lesson *settings* (title, objectives, minutes…) still change immediately. Only blocks are staged,
  because blocks hold the teaching content.
- Media URLs inserted from the library are absolute (like WordPress), built from the request host.
  In production, media files must be served by the web server or object storage; Django serves
  `/media/` only when `DEBUG` is on.
