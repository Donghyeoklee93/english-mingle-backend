from .models import Photo, Video
from .serializers import PhotoSerializer, VideoSerializer
from rest_framework.viewsets import ModelViewSet


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
