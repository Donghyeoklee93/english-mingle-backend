from dataclasses import fields
from rest_framework import serializers
from .models import Booking
from django.utils import timezone


class CreateChallengeBookingSerializer(serializers.ModelSerializer):
    time_from = serializers.DateField()
    time_to = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "time_from",
            "time_to",
        )

    def validate_time_from(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_time_to(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):
        challenge = self.context.get("challenge")

        if data["time_to"] <= data["time_from"]:
            raise serializers.ValidationError(
                "Start date should be smaller than finish date."
            )
        if Booking.objects.filter(
            challenge=challenge,
            time_from__lte=data["time_to"],
            time_to__gte=data["time_from"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


class CreateOfflineBookingSerializer(serializers.ModelSerializer):
    time_from = serializers.DateField()
    time_to = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "time_from",
            "time_to",
        )

    def validate_time_from(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_time_to(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):
        offline = self.context.get("offline")

        if data["time_to"] <= data["time_from"]:
            raise serializers.ValidationError(
                "Start date should be smaller than finish date."
            )
        if Booking.objects.filter(
            offline=offline,
            time_from__lte=data["time_to"],
            time_to__gte=data["time_from"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


class CreateOnlineBookingSerializer(serializers.ModelSerializer):
    time_from = serializers.DateField()
    time_to = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "time_from",
            "time_to",
        )

    def validate_time_from(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_time_to(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):
        online = self.context.get("offline")

        if data["time_to"] <= data["time_from"]:
            raise serializers.ValidationError(
                "Start date should be smaller than finish date."
            )
        if Booking.objects.filter(
            online=online,
            time_from__lte=data["time_to"],
            time_to__gte=data["time_from"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "kind",
            "user",
            "online",
            "offline",
            "challenge",
            "time_from",
            "time_to",
        )
