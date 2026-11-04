from django.contrib import admin

from .models import Attempt, Choice, PracticeSet, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    fields = (("order", "concept", "skill"), "prompt", "feedback")
    show_change_link = True


@admin.register(PracticeSet)
class PracticeSetAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "status", "order")
    list_editable = ("status", "order")
    list_filter = ("status", "topic__module__course__offering__level", "topic__module__course")
    list_select_related = ("topic",)
    search_fields = ("title", "topic__title")
    autocomplete_fields = ("topic", "lesson")
    inlines = [QuestionInline]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 8
    fields = ("order", "text", "is_correct", "why_wrong")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "practice_set", "concept", "order")
    list_filter = ("practice_set__topic__module__course",)
    list_select_related = ("practice_set",)
    search_fields = ("prompt", "concept")
    autocomplete_fields = ("practice_set",)
    inlines = [ChoiceInline]


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "practice_set", "correct_count", "total", "completed_at")
    list_select_related = ("user", "practice_set")
    search_fields = ("user__email", "practice_set__title")
    readonly_fields = ("user", "practice_set", "started_at", "completed_at", "correct_count", "total")
