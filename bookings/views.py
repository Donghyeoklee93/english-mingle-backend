from .models import Booking
from .serializers import BookingSerializer
from rest_framework.viewsets import ModelViewSet


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
