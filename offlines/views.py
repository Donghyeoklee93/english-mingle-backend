from .models import Offline
from .serializers import OfflineSerializer
from rest_framework.viewsets import ModelViewSet


class OfflineViewSet(ModelViewSet):
    serializer_class = OfflineSerializer
    queryset = Offline.objects.all()
