from dataclasses import fields
from rest_framework import serializers
from .models import Photo, Video


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "pk",
            "file",
            "description",
            "online",
            "offline",
            "challenge",
            "created_at",
            "updated_at",
        )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "pk",
            "file",
            "offline",
            "created_at",
            "updated_at",
        )
