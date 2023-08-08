from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Challenge
from users.serializers import TinyUserSerializer
from levels.serializers import LevelSerializer
from subjects.serializers import SubjectSerializer
from medias.serializers import PhotoSerializer


class ChallengeDetailSerializer(ModelSerializer):
    tutor = TinyUserSerializer(read_only=True)
    subjects = SubjectSerializer(read_only=True, many=True)
    level = LevelSerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = "__all__"
        # depth = 1

    def get_rating(self, challenge):
        return challenge.rating()

    def get_is_owner(self, challenge):
        request = self.context.get("request")
        if request:
            return challenge.tutor == request.user
        return False

    def get_reviews_count(self, challenge):
        return challenge.reviews.count()


class ChallengeListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = (
            "pk",
            "name",
            # "tutor",
            "description",
            "price",
            "kind",
            "rating",
            "is_owner",
            "reviews_count",
            "photos",
            "start",
            "end",
        )

    def get_rating(self, challenge):
        return challenge.rating()

    def get_is_owner(self, challenge):
        request = self.context.get("request")
        if request:
            return challenge.tutor == request.user
        return False

    def get_reviews_count(self, challenge):
        return challenge.reviews.count()
