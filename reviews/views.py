from .models import Review
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
