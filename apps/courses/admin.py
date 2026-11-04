from django.contrib import admin

from .models import Course, CourseResource, Lesson, LessonBlock, Module, Topic


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0
    fields = ("order", "title", "summary")
    show_change_link = True


class CourseResourceInline(admin.TabularInline):
    model = CourseResource
    extra = 0
    fields = ("order", "title", "kind", "url", "file", "detail")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
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


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0
    fields = ("order", "title", "summary")
    show_change_link = True


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_editable = ("order",)
    list_filter = ("course__offering__level", "course__offering__subject", "course")
    list_select_related = ("course",)
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)
    inlines = [TopicInline]


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "slug", "lesson_type", "estimated_minutes", "status")
    prepopulated_fields = {"slug": ("title",)}
    show_change_link = True


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
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


class LessonBlockInline(admin.StackedInline):
    model = LessonBlock
    extra = 0
    fields = (("order", "block_type"), "title", "body", ("media_url", "alt_text"), "data")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
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
