from dataclasses import fields
from rest_framework import serializers
from .models import Offline


class OfflineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offline
        fields = (
            "name",
            "tutor",
            "price",
            "description",
            "subject",
            "level",
        )
