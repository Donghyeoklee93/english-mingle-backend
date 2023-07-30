from dataclasses import fields
from rest_framework import serializers
from .models import ChattingRoom


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingRoom
        fields = ("users",)
