from .models import Photo
from .serializers import MediaSerializer
from rest_framework.viewsets import ModelViewSet


class MediaViewSet(ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Photo.objects.all()
