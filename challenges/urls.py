from django.urls import path
from . import views

urlpatterns = [
    path("", views.Challenges.as_view()),
    path("<int:pk>", views.ChallengeDetail.as_view()),
    path("<int:pk>/reviews", views.ChallengeReviews.as_view()),
    path("<int:pk>/photos", views.ChallengePhotos.as_view()),
    path("<int:pk>/bookings", views.ChallengeBookings.as_view()),
]
