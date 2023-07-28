from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "classes",
        "event",
        "challenge",
        "time_from",
        "time_to",
        "event_time",
    )

    list_filter = ("kind",)
