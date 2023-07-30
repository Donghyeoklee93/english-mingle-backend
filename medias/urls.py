from django.urls import path
from . import views

urlpatterns = [
    path(
        "photoes",
        views.PhotoViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "photoes/<int:pk>",
        views.PhotoViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
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
