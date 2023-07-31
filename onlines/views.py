from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Online
from .serializers import OnlineListSerializer, OnlineDetailSerializer


class Onlines(APIView):
    def get(self, request):
        all_onlines = Online.objects.all()
        serializer = OnlineListSerializer(all_onlines, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = OnlineDetailSerializer(data=request.data)
            if serializer.is_valid():
                online = serializer.save(tutor=request.user)
                serializer = OnlineDetailSerializer(online)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class OnlinesDetail(APIView):
    def get_object(self, pk):
        try:
            return Online.objects.get(pk=pk)
        except Online.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        online = self.get_object(pk)
        serializer = OnlineDetailSerializer(online)
        return Response(serializer.data)


# class OnlineViewSet(ModelViewSet):
#     serializer_class = OnlineSerializer
#     queryset = Online.objects.all()
