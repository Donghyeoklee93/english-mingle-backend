from .models import Level
from .serializers import LevelSerializer
from rest_framework.viewsets import ModelViewSet


class LevelViewSet(ModelViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
