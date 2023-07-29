from django.contrib import admin
from .models import Online, Subject


@admin.action(description="Set all price to zero")
def reset_price(model_admin, request, onlines):
    for online in onlines:
        online.price = 0
        online.save()


@admin.register(Online)
class ClassAdmin(admin.ModelAdmin):
    actions = (reset_price,)

    list_display = (
        "name",
        "price",
        "kind",
        "tutor",
        "rating",
    )

    list_filter = (
        "name",
        "price",
        "kind",
        "tutor",
        "subject",
        "created_at",
        "updated_at",
        "level",
    )

    search_fields = [
        "name",
        "^tutor__username",
    ]


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