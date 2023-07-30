from .models import ChattingRoom, Messenger
from .serializers import ChattingRoomSerializer, MessengerSerializer
from rest_framework.viewsets import ModelViewSet


class MessengerViewSet(ModelViewSet):
    serializer_class = MessengerSerializer
    queryset = Messenger.objects.all()


class ChattingRoomViewSet(ModelViewSet):
    serializer_class = ChattingRoomSerializer
    queryset = ChattingRoom.objects.all()
