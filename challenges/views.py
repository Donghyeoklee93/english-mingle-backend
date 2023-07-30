from .models import Challenge
from .serializers import ChallengeSerializer
from rest_framework.viewsets import ModelViewSet


class ChallengeViewSet(ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
