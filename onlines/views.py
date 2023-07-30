from .models import Online
from .serializers import OnlineSerializer
from rest_framework.viewsets import ModelViewSet


class OnlineViewSet(ModelViewSet):
    serializer_class = OnlineSerializer
    queryset = Online.objects.all()
