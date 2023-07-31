from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Online
from users.serializers import TinyUserSerializer
from levels.serializers import LevelSerializer
from subjects.serializers import SubjectSerializer


class OnlineDetailSerializer(ModelSerializer):
    tutor = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True, many=True)
    level = LevelSerializer(
        read_only=True,
    )

    class Meta:
        model = Online
        fields = "__all__"
        # depth = 1


class OnlineListSerializer(ModelSerializer):
    class Meta:
        model = Online
        fields = (
            "pk",
            "name",
            # "tutor",
            "price",
            "description",
        )


# class OnlineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Online
#         fields = (
#             "name",
#             "tutor",
#             "price",
#             "description",
#             "kind",
#             "subject",
#             "level",
#         )
