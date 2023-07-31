from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Offline
from .serializers import OfflineListSerializer, OfflineDetailSerializer


class Offlines(APIView):
    def get(self, request):
        all_offlines = Offline.objects.all()
        serializer = OfflineListSerializer(all_offlines, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = OfflineDetailSerializer(data=request.data)
            if serializer.is_valid():
                offline = serializer.save(tutor=request.user)
                serializer = OfflineDetailSerializer(offline)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class OfflineDetail(APIView):
    def get_object(self, pk):
        try:
            return Offline.objects.get(pk=pk)
        except Offline.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        Offline = self.get_object(pk)
        serializer = OfflineDetailSerializer(Offline)
        return Response(serializer.data)
