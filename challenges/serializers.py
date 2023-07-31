from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Challenge
from users.serializers import TinyUserSerializer
from levels.serializers import LevelSerializer
from subjects.serializers import SubjectSerializer


class ChallengeDetailSerializer(ModelSerializer):
    tutor = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True, many=True)
    level = LevelSerializer(
        read_only=True,
    )

    class Meta:
        model = Challenge
        fields = "__all__"
        # depth = 1


class ChallengeListSerializer(ModelSerializer):
    class Meta:
        model = Challenge
        fields = (
            "pk",
            "name",
            # "tutor",
            "price",
            "kind",
        )


# class ChallengeSerializer(ModelSerializer):
#     class Meta:
#         model = Challenge
#         fields = "__all__"
#         depth = 1


# class ChallengeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Challenge
#         fields = (
#             "pk",
#             "name",
#             "tutor",
#             "price",
#             "description",
#             "kind",
#             "start",
#             "end",
#             "subject",
#             "level",
#             "created_at",
#             "updated_at",
#         )
