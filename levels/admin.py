from django.contrib import admin
from .models import Level


@admin.register(Level)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
