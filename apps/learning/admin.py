from django.contrib import admin

from .models import DailyActivity, Enrollment, LessonNote, LessonProgress, SavedLesson, StudySession


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "offering", "created_at")
    list_filter = ("offering__level", "offering__subject")
    list_select_related = ("user", "offering__subject", "offering__level")
    search_fields = ("user__email", "offering__subject__name")
    autocomplete_fields = ("user", "offering")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "percent", "completed_at", "last_viewed_at")
    list_filter = ("completed_at", "lesson__topic__module__course")
    list_select_related = ("user", "lesson")
    search_fields = ("user__email", "lesson__title")
    autocomplete_fields = ("user", "lesson")


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "kind", "starts_at", "duration_minutes", "completed_at")
    list_filter = ("kind", "subject")
    list_select_related = ("user", "subject")
    search_fields = ("title", "user__email")
    autocomplete_fields = ("user", "subject", "lesson", "topic")


admin.site.register(DailyActivity, list_display=("user", "date", "seconds"), list_filter=("date",))
admin.site.register(SavedLesson, list_display=("user", "lesson", "created_at"))
admin.site.register(LessonNote, list_display=("user", "lesson", "video_time", "created_at"))
