from .models import ChattingRoom
from .serializers import MessengerSerializer
from rest_framework.viewsets import ModelViewSet


class MessengerViewSet(ModelViewSet):
    serializer_class = MessengerSerializer
    queryset = ChattingRoom.objects.all()
