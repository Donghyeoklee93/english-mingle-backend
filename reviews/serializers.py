from dataclasses import fields
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "pk",
            "user",
            # "online",
            # "offline",
            # "challenge",
            "textArea",
            "rating",
        )
        depth = 1
