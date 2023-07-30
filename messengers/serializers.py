from dataclasses import fields
from rest_framework import serializers
from .models import ChattingRoom, Messenger


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = (
            "text",
            "user",
            "room",
        )


class ChattingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingRoom
        fields = ("users",)
