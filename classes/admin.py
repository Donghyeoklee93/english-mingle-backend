from django.contrib import admin
from .models import Class, Subject


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "tutor",
    )

    list_filter = (
        "name",
        "price",
        "kind",
        "tutor",
        "subjects",
        "created_at",
        "updated_at",
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
