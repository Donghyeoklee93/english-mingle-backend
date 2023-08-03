from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            "pk",
            "name",
            "description",
            # "created_at",
            # "updated_at",
        )
