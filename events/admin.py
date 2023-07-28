from django.contrib import admin
from .models import Event

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "tutor",
        "price",
        # "description",
        "address",
    ]

    list_filter = [
        "price",
        "level",
    ]

    search_fields = [
        "name",
    ]
