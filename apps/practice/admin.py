from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from .models import Attempt, Choice, MistakeCard, PracticeSet, Question, ReviewSession


class QuestionInline(StackedInline):
    model = Question
    extra = 0
    fields = (("order", "kind", "concept", "skill"), "prompt", "hint", "feedback")
    show_change_link = True


@admin.register(PracticeSet)
class PracticeSetAdmin(ModelAdmin):
    list_display = ("title", "topic", "status", "order")
    list_editable = ("status", "order")
    list_filter = ("status", "topic__module__course__offering__level", "topic__module__course")
    list_select_related = ("topic",)
    search_fields = ("title", "topic__title")
    autocomplete_fields = ("topic", "lesson")
    inlines = [QuestionInline]


class ChoiceInline(TabularInline):
    model = Choice
    extra = 4
    max_num = 8
    fields = ("order", "text", "is_correct", "why_wrong")


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("__str__", "practice_set", "kind", "concept", "has_hint", "order")
    list_filter = ("kind", "practice_set__topic__module__course")
    list_select_related = ("practice_set",)
    search_fields = ("prompt", "concept")
    autocomplete_fields = ("practice_set",)
    inlines = [ChoiceInline]
    fieldsets = (
        (None, {"fields": ("practice_set", ("order", "kind"), "prompt", ("concept", "skill"),
                           ("diagram_url", "diagram_alt"))}),
        ("Hint", {"fields": ("hint",), "description": "Optional. Students can open it before answering; "
                  "we record that they did."}),
        ("Numeric answer", {"fields": (("numeric_answer", "tolerance", "unit"),),
                            "description": "Only for “Numeric answer” questions. Leave the choices below empty."}),
        ("Feedback", {"fields": ("feedback", "solution_steps")}),
    )

    @admin.display(boolean=True, description="Hint")
    def has_hint(self, obj):
        return bool(obj.hint)


@admin.register(Attempt)
class AttemptAdmin(ModelAdmin):
    list_display = ("user", "practice_set", "mode", "correct_count", "total", "completed_at")
    list_filter = ("mode",)
    list_select_related = ("user", "practice_set")
    search_fields = ("user__email", "practice_set__title")
    readonly_fields = ("user", "practice_set", "mode", "time_limit_seconds", "hints_used", "started_at",
                       "completed_at", "correct_count", "total")


@admin.register(MistakeCard)
class MistakeCardAdmin(ModelAdmin):
    list_display = ("user", "question", "step", "due_on", "reviews", "retired_at")
    list_filter = ("step",)
    list_select_related = ("user", "question")
    search_fields = ("user__email", "question__prompt")
    readonly_fields = ("user", "question", "last_missed_at", "reviews")


@admin.register(ReviewSession)
class ReviewSessionAdmin(ModelAdmin):
    list_display = ("user", "started_at", "completed_at")
    list_select_related = ("user",)
    search_fields = ("user__email",)
    readonly_fields = ("user", "question_ids", "hints_used", "started_at", "completed_at")
