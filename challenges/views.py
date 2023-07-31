from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Challenge
from .serializers import ChallengeListSerializer, ChallengeDetailSerializer


class Challenges(APIView):
    def get(self, request):
        all_challenges = Challenge.objects.all()
        serializer = ChallengeListSerializer(all_challenges, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = ChallengeDetailSerializer(data=request.data)
            if serializer.is_valid():
                challenge = serializer.save(tutor=request.user)
                serializer = ChallengeDetailSerializer(challenge)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class ChallengeDetail(APIView):
    def get_object(self, pk):
        try:
            return Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        Challenge = self.get_object(pk)
        serializer = ChallengeDetailSerializer(Challenge)
        return Response(serializer.data)


# class ChallengeViewSet(ModelViewSet):
#     serializer_class = ChallengeSerializer
#     queryset = Challenge.objects.all()
