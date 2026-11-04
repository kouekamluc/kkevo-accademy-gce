from django.contrib import admin

from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "offering", "created_at")
    list_filter = ("offering__level", "offering__subject")
    list_select_related = ("user", "offering__subject", "offering__level")
    search_fields = ("user__email", "offering__subject__name")
    autocomplete_fields = ("user", "offering")
