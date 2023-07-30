from dataclasses import fields
from rest_framework import serializers
from .models import Photo, Video


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "file",
            "description",
            "online",
            "Offline",
            "challenge",
        )


# class MediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = (
#             "file",
#             "offline",
#         )
