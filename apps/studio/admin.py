from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html

from .models import LessonDraft, LessonEvent, LessonRevision, MediaAsset


class ReadOnlyAdmin(ModelAdmin):
    """History must not be rewritten: these records are created by the studio only."""

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(LessonEvent)
class LessonEventAdmin(ReadOnlyAdmin):
    list_display = ("created_at", "lesson", "action", "actor", "from_status", "to_status", "short_comment")
    list_filter = ("action", "created_at")
    list_select_related = ("lesson", "actor")
    search_fields = ("lesson__title", "comment", "actor__email")
    date_hierarchy = "created_at"

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    @admin.display(description="Comment")
    def short_comment(self, obj):
        return (obj.comment[:80] + "…") if len(obj.comment) > 80 else obj.comment


@admin.register(LessonRevision)
class LessonRevisionAdmin(ReadOnlyAdmin):
    list_display = ("lesson", "number", "kind", "created_by", "created_at", "block_count")
    list_filter = ("kind",)
    list_select_related = ("lesson", "created_by")
    search_fields = ("lesson__title", "note")

    @admin.display(description="Blocks")
    def block_count(self, obj):
        return len(obj.blocks or [])


@admin.register(LessonDraft)
class LessonDraftAdmin(ReadOnlyAdmin):
    list_display = ("lesson", "status", "created_by", "updated_at", "editor_link")
    list_filter = ("status",)
    list_select_related = ("lesson", "created_by")

    @admin.display(description="Studio")
    def editor_link(self, obj):
        return format_html('<a href="/studio/lessons/{}/">Open in studio</a>', obj.lesson_id)


@admin.register(MediaAsset)
class MediaAssetAdmin(ModelAdmin):
    list_display = ("title", "content_type", "size", "uploaded_by", "created_at")
    search_fields = ("title", "alt_text")
    list_select_related = ("uploaded_by",)
    readonly_fields = ("file", "content_type", "size", "uploaded_by", "created_at")
    fields = ("title", "alt_text", "file", "content_type", "size", "uploaded_by", "created_at")

    def has_add_permission(self, request):
        return False  # uploads go through the studio, which validates the file
