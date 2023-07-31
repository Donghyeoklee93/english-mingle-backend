from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import Challenge
from subjects.models import Subject
from levels.models import Level
from .serializers import ChallengeListSerializer, ChallengeDetailSerializer
from reviews.serializers import ReviewSerializer
from django.conf import settings
from medias.serializers import PhotoSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bookings.models import Booking
from bookings.serializers import BookingSerializer, CreateChallengeBookingSerializer


class Challenges(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_challenges = Challenge.objects.all()
        serializer = ChallengeListSerializer(
            all_challenges,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ChallengeDetailSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            level_pk = request.data.get("level")
            if not level_pk:
                raise ParseError("Level is required.")
            try:
                level = Level.objects.get(pk=level_pk)
            except Level.DoesNotExist:
                raise ParseError("Level is not found")

            try:
                with transaction.atomic():
                    challenge = serializer.save(
                        tutor=request.user,
                        level=level,
                    )
                    subjects = request.data.get("subjects")
                    for subject_pk in subjects:
                        subject = Subject.objects.get(pk=subject_pk)
                        challenge.subjects.add(subject)
                    serializer = ChallengeDetailSerializer(challenge)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Subject is not found")
        else:
            return Response(serializer.errors)


class ChallengeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        challenge = self.get_object(pk)
        serializer = ChallengeDetailSerializer(
            challenge,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        challenge = self.get_object(pk)
        if challenge.tutor != request.user:
            raise PermissionDenied
        serializer = ChallengeDetailSerializer(
            challenge,
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
                            challenge.subjects.add(subject)
                    else:
                        challenge.subjects.clear()

                    return Response(ChallengeDetailSerializer(challenge).data)
            except Exception as e:
                print(e)
                raise ParseError("subjects not found")
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        challenge = self.get_object(pk)

        if challenge.tutor != request.user:
            raise PermissionDenied
        challenge.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# class ChallengeViewSet(ModelViewSet):
#     serializer_class = ChallengeSerializer
#     queryset = Challenge.objects.all()


class ChallengeReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Challenge.objects.get(pk=pk)
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

        challenge = self.get_object(pk)
        serializer = ReviewSerializer(
            challenge.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                challenge=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            Response(serializer.errors)


class ChallengePhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Challenge.objects.get(pk=pk)
        except:
            raise NotFound

    def post(self, request, pk):
        challenge = self.get_object(pk)

        if challenge.tutor != request.user:
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():
            photo = serializer.save(
                challenge=challenge,
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        pass


class ChallengeBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        challenge = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            challenge=challenge,
            kind=Booking.BookingKindChoices.CHALLENGE,
            time_from__gt=now,
        )
        serializer = BookingSerializer(
            bookings,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request, pk):
        challenge = self.get_object(pk)
        serializer = CreateChallengeBookingSerializer(
            data=request.data,
            context={"challenge": challenge},
        )
        if serializer.is_valid():
            booking = serializer.save(
                challenge=challenge,
                user=request.user,
                kind=Booking.BookingKindChoices.CHALLENGE,
            )
            serializer = BookingSerializer(booking)
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
