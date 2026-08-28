from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "salary",
        "created_at",
    )

    search_fields = (
        "title",
        "company",
        "location",
        "description",
    )

    list_filter = (
        "company",
        "location",
        "created_at",
    )

    ordering = ("-created_at",)

    readonly_fields = ("job_id", "created_at")

    fieldsets = (
        ("Job Information", {
            "fields": (
                "job_id",
                "title",
                "company",
                "description",
                "commitment",
                "Experience",
                "requirements",
            )
        }),
        ("Location & Compensation", {
            "fields": (
                "location",
                "salary",
            )
        }),
        ("System Information", {
            "fields": (
                "created_at",
            )
        }),
    )