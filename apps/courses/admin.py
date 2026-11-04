from django.contrib import admin
from django.shortcuts import redirect
from unfold.decorators import action
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from .models import Course, CourseResource, Lesson, LessonBlock, Module, Topic


class ModuleInline(TabularInline):
    model = Module
    extra = 0
    fields = ("order", "title", "summary")
    show_change_link = True


class CourseResourceInline(TabularInline):
    model = CourseResource
    extra = 0
    fields = ("order", "title", "kind", "url", "file", "detail")


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("title", "subject_name", "level_name", "status", "order", "updated_at")
    list_editable = ("status", "order")
    list_filter = ("status", "offering__level", "offering__pathways", "offering__subject")
    list_select_related = ("offering__subject", "offering__level")
    search_fields = ("title", "summary", "offering__subject__name")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("offering",)
    inlines = [ModuleInline, CourseResourceInline]

    @admin.display(description="Subject", ordering="offering__subject__name")
    def subject_name(self, obj):
        return obj.offering.subject.name

    @admin.display(description="Level", ordering="offering__level__order")
    def level_name(self, obj):
        return obj.offering.level.name


class TopicInline(TabularInline):
    model = Topic
    extra = 0
    fields = ("order", "title", "summary")
    show_change_link = True


@admin.register(Module)
class ModuleAdmin(ModelAdmin):
    list_display = ("title", "course", "order")
    list_editable = ("order",)
    list_filter = ("course__offering__level", "course__offering__subject", "course")
    list_select_related = ("course",)
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)
    inlines = [TopicInline]


class LessonInline(TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "slug", "lesson_type", "estimated_minutes", "status")
    prepopulated_fields = {"slug": ("title",)}
    show_change_link = True


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = ("title", "module", "course_title", "order")
    list_editable = ("order",)
    list_filter = ("module__course__offering__level", "module__course")
    list_select_related = ("module__course",)
    search_fields = ("title", "module__title", "module__course__title")
    autocomplete_fields = ("module", "curriculum_references")
    inlines = [LessonInline]

    @admin.display(description="Course", ordering="module__course__title")
    def course_title(self, obj):
        return obj.module.course.title


class LessonBlockInline(StackedInline):
    model = LessonBlock
    extra = 0
    fields = (("order", "block_type"), "title", "body", ("media_url", "alt_text"), "data")
    verbose_name_plural = "Lesson blocks (published lessons: edit in the content studio so changes are reviewed)"

    @staticmethod
    def _locked(request, obj):
        # Blocks of a published lesson are what students see: only the studio's draft/review flow may change them.
        return obj is not None and obj.status == "published" and not request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return not self._locked(request, obj) and super().has_add_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        return not self._locked(request, obj) and super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return not self._locked(request, obj) and super().has_delete_permission(request, obj)


@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ("title", "topic", "lesson_type", "estimated_minutes", "status", "author", "order")
    list_editable = ("status", "order")
    list_filter = ("status", "lesson_type", "topic__module__course__offering__level", "topic__module__course")
    list_select_related = ("topic",)
    search_fields = ("title", "summary", "topic__title")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("topic", "curriculum_references", "prerequisites", "author", "reviewer")
    fieldsets = (
        (None, {"fields": ("topic", "title", "slug", "summary", ("lesson_type", "estimated_minutes"), "order")}),
        ("Learning design", {"fields": ("objectives", "key_concepts", "prerequisites", "curriculum_references")}),
        ("Workflow", {"fields": ("status", "author", "reviewer")}),
    )
    inlines = [LessonBlockInline]
    # Lesson content is written in the studio; these buttons keep staff in one workflow.
    actions_detail = ["edit_in_studio"]
    actions_row = ["edit_in_studio"]

    @action(description="Edit in studio", icon="edit_note", url_path="edit-in-studio")
    def edit_in_studio(self, request, object_id):
        return redirect("studio:edit", pk=object_id)
