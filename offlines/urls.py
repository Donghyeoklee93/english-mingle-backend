from django.urls import path
from . import views

urlpatterns = [
    path("", views.Offlines.as_view()),
    path("<int:pk>", views.OfflineDetail.as_view()),
    path("<int:pk>/reviews", views.OfflineReviews.as_view()),
    path("<int:pk>/photos", views.OfflinePhotos.as_view()),
    path("<int:pk>/bookings", views.OfflineBookings.as_view()),
]
