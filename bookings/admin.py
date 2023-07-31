from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "kind",
        "user",
        "online",
        "offline",
        "challenge",
        "time_from",
        "time_to",
        "created_at",
        "updated_at",
    )

    list_filter = ("kind",)
