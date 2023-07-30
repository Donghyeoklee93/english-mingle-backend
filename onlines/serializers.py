from dataclasses import fields
from rest_framework import serializers
from .models import Online


class OnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online
        fields = (
            "tutor",
            "price",
            "description",
            "kind",
            "subject",
            "level",
        )
