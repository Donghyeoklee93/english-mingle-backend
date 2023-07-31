from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Offline
from users.serializers import TinyUserSerializer
from levels.serializers import LevelSerializer
from subjects.serializers import SubjectSerializer
from medias.serializers import PhotoSerializer


class OfflineDetailSerializer(ModelSerializer):
    tutor = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True, many=True)
    level = LevelSerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Offline
        fields = "__all__"
        # depth = 1

    def get_rating(self, offline):
        return offline.rating()

    def get_is_owner(self, offline):
        request = self.context.get("request")
        if request:
            return offline.tutor == request.user
        return False

    def get_reviews_count(self, offline):
        return offline.reviews.count()


class OfflineListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Offline
        fields = (
            "pk",
            "name",
            # "tutor",
            "price",
            "description",
            "rating",
            "is_owner",
            "reviews_count",
            "photos",
        )

    def get_rating(self, offline):
        return offline.rating()

    def get_is_owner(self, offline):
        request = self.context.get("request")
        if request:
            return offline.tutor == request.user
        return False

    def get_reviews_count(self, offline):
        return offline.reviews.count()


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
