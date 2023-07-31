from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Offline
from users.serializers import TinyUserSerializer
from levels.serializers import LevelSerializer
from subjects.serializers import SubjectSerializer


class OfflineDetailSerializer(ModelSerializer):
    tutor = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True, many=True)
    level = LevelSerializer(
        read_only=True,
    )

    class Meta:
        model = Offline
        fields = "__all__"
        # depth = 1


class OfflineListSerializer(ModelSerializer):
    class Meta:
        model = Offline
        fields = (
            "pk",
            "name",
            # "tutor",
            "price",
            "description",
        )


# from rest_framework import serializers
# from .models import Offline

# class OfflineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Offline
#         fields = (
#             "name",
#             "tutor",
#             "price",
#             "description",
#             "subject",
#             "level",
#         )
