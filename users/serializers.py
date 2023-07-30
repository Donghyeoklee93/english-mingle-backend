from dataclasses import fields
from rest_framework import serializers
from .models import User


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "avatar",
            "name",
            "is_host",
            "gender",
        )
