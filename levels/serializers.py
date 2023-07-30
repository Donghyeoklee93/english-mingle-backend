from dataclasses import fields
from rest_framework import serializers
from .models import Level


class LevelSerializer(serializers.Serializer):
    class Meta:
        model = Level
        fields = (
            "pk",
            "name",
            "kind",
        )
