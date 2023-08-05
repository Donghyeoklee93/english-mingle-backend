from django.urls import path
from . import views

urlpatterns = [
    path("", views.Onlines.as_view()),
    path("<int:pk>", views.OnlineDetail.as_view()),
    path("<int:pk>/reviews", views.OnlineReviews.as_view()),
    path("<int:pk>/photos", views.OnlinePhotos.as_view()),
    path("<int:pk>/bookings", views.OnlineBookings.as_view()),
    path("<int:pk>/bookings/check", views.OnlineBookingCheck.as_view()),
]
