from dataclasses import fields
from rest_framework import serializers
from .models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = (
            "pk",
            "name",
            "tutor",
            "price",
            "description",
            "kind",
            "start",
            "end",
            "subject",
            "level",
            "created_at",
            "updated_at",
        )
