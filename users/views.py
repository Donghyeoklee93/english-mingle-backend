from .models import User
from .serializers import MessengerSerializer
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = MessengerSerializer
    queryset = User.objects.all()
