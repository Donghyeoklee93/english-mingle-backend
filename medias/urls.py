from django.urls import path
from . import views

urlpatterns = [
    path(
        "photos/get-url",
        views.GetUploadURL.as_view(),
    ),
    path(
        "photos/<int:pk>",
        views.PhotoDetail.as_view(),
    ),
    path(
        "videos",
        views.VideoViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "videos/<int:pk>",
        views.VideoViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
    ),
]
