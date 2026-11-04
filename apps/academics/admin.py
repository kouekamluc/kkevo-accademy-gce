from django.contrib import admin

from .models import (
    AcademicLevel,
    AcademicPathway,
    CurriculumReference,
    Subject,
    SubjectOffering,
    Syllabus,
)


@admin.register(AcademicLevel)
class AcademicLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "exam_level", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("exam_level", "is_active")
    search_fields = ("name", "code")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(AcademicPathway)
class AcademicPathwayAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class SubjectOfferingInline(admin.TabularInline):
    model = SubjectOffering
    extra = 0
    fields = ("level", "pathways", "is_active")
    autocomplete_fields = ("level",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_text", "accent", "is_featured", "order", "is_active")
    list_editable = ("is_featured", "order", "is_active")
    list_filter = ("accent", "is_featured", "is_active", "offerings__level", "offerings__pathways")
    search_fields = ("name", "summary")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SubjectOfferingInline]


@admin.register(SubjectOffering)
class SubjectOfferingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "subject", "level", "pathway_list", "is_active")
    list_filter = ("level", "pathways", "is_active")
    list_select_related = ("subject", "level")
    search_fields = ("subject__name", "level__name")
    autocomplete_fields = ("subject", "level")
    filter_horizontal = ("pathways",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("pathways")

    @admin.display(description="Pathways")
    def pathway_list(self, obj):
        return ", ".join(p.name for p in obj.pathways.all())


class CurriculumReferenceInline(admin.TabularInline):
    model = CurriculumReference
    extra = 0
    fields = ("code", "title", "parent", "order")
    ordering = ("order", "code")


@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ("__str__", "version", "is_official", "status", "effective_from", "effective_to")
    list_filter = ("status", "is_official", "offering__level", "offering__subject")
    list_select_related = ("offering__subject", "offering__level")
    search_fields = ("title", "version", "offering__subject__name")
    autocomplete_fields = ("offering",)
    inlines = [CurriculumReferenceInline]


@admin.register(CurriculumReference)
class CurriculumReferenceAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "syllabus", "parent", "order")
    list_filter = ("syllabus__offering__level", "syllabus__offering__subject", "syllabus")
    list_select_related = ("syllabus__offering__subject", "syllabus__offering__level", "parent")
    search_fields = ("code", "title")
    autocomplete_fields = ("syllabus", "parent")
