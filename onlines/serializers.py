from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from medias.serializers import PhotoSerializer
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

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Online
        fields = "__all__"
        # depth = 1

    def get_rating(self, online):
        return online.rating()

    def get_is_owner(self, online):
        request = self.context.get("request")
        if request:
            return online.tutor == request.user
        return False

    def get_reviews_count(self, online):
        return online.reviews.count()


class OnlineListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Online
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

    def get_rating(self, online):
        return online.rating()

    def get_is_owner(self, online):
        request = self.context.get("request")
        if request:
            return online.tutor == request.user
        return False

    def get_reviews_count(self, online):
        return online.reviews.count()
