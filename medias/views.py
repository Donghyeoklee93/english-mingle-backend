from .models import Photo, Video
from .serializers import PhotoSerializer, VideoSerializer
from rest_framework.viewsets import ModelViewSet


import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Photo


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)

        if (
            (photo.challenge and photo.challenge.tutor != request.user)
            or (photo.online and photo.online.tutor != request.user)
            or (photo.offline and photo.offline.tutor != request.user)
        ):
            raise PermissionDenied

        photo.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"

        one_time_url = requests.post(
            url,
            headers={"Authorization": f"Bearer {settings.CF_TOKEN}"},
        )

        one_time_url = one_time_url.json()
        result = one_time_url.get("result")

        return Response({"uploadURL": result.get("uploadURL")})


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
