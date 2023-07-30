from dataclasses import fields
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "kind",
            "user",
            "online",
            "offline",
            "challenge",
            "time_from",
            "time_to",
            "online_offline_time",
        )
