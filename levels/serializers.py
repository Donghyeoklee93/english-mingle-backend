from dataclasses import fields
from rest_framework import serializers
from .models import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            "pk",
            "name",
            "kind",
            "created_at",
            "updated_at",
        )
