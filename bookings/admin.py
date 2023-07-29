from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "online",
        "offline",
        "challenge",
        "time_from",
        "time_to",
        "online_offline_time",
    )

    list_filter = ("kind",)
