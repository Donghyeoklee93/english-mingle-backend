from django.db import transaction
from django.conf import settings
from django.utils import timezone


from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)

from levels.models import Level
from subjects.models import Subject
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.models import Booking
from bookings.serializers import BookingSerializer, CreateOnlineBookingSerializer


from .models import Online
from .serializers import OnlineListSerializer, OnlineDetailSerializer


class Onlines(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_onlines = Online.objects.all()
        serializer = OnlineListSerializer(
            all_onlines,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = OnlineDetailSerializer(data=request.data)
        if serializer.is_valid():
            level_pk = request.data.get("level")
            if not level_pk:
                raise ParseError("Level is required.")
            try:
                level = Level.objects.get(pk=level_pk)
            except Level.DoesNotExist:
                raise ParseError("Level is not found")

            try:
                with transaction.atomic():
                    online = serializer.save(
                        tutor=request.user,
                        level=level,
                    )
                    subjects = request.data.get("subjects")
                    for subject_pk in subjects:
                        subject = Subject.objects.get(pk=subject_pk)
                        online.subjects.add(subject)
                    serializer = OnlineDetailSerializer(online)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Subject is not found")
        else:
            return Response(serializer.errors)


class OnlineDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Online.objects.get(pk=pk)
        except Online.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        Online = self.get_object(pk)
        serializer = OnlineDetailSerializer(
            Online,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        online = self.get_object(pk)
        if online.tutor != request.user:
            raise PermissionDenied
        serializer = OnlineDetailSerializer(
            online,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            level_pk = request.data.get("level")
            if level_pk:
                try:
                    level = Level.objects.get(pk=level_pk)
                except Level.DoesNotExist:
                    raise ParseError(detail="level not found")

            try:
                with transaction.atomic():
                    if level_pk:
                        room = serializer.save(category=level)
                    else:
                        room = serializer.save()

                    subjects = request.data.get("subjects")
                    if subjects:
                        room.subjects.clear()
                        for subject_pk in subjects:
                            subject = Subject.objects.get(pk=subject_pk)
                            online.subjects.add(subject)
                    else:
                        online.subjects.clear()

                    return Response(OnlineDetailSerializer(online).data)
            except Exception as e:
                print(e)
                raise ParseError("subjects not found")
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        online = self.get_object(pk)

        if online.tutor != request.user:
            raise PermissionDenied
        online.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class OnlineReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Online.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        online = self.get_object(pk)
        serializer = ReviewSerializer(
            online.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                online=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            Response(serializer.errors)


class OnlinePhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Offline.objects.get(pk=pk)
        except:
            raise NotFound

    def post(self, request, pk):
        offline = self.get_object(pk)

        if offline.tutor != request.user:
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():
            photo = serializer.save(
                offline=offline,
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        pass


class OnlineBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Online.objects.get(pk=pk)
        except Online.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        online = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            online=online,
            kind=Booking.BookingKindChoices.ONLINE,
            time_from__gt=now,
        )
        serializer = BookingSerializer(
            bookings,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request, pk):
        online = self.get_object(pk)
        serializer = CreateOnlineBookingSerializer(
            data=request.data,
            context={"online": online},
        )
        if serializer.is_valid():
            booking = serializer.save(
                online=online,
                user=request.user,
                kind=Booking.BookingKindChoices.ONLINE,
            )
            serializer = BookingSerializer(booking)
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
