from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.MessengerViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.MessengerViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
    ),
    path(
        "<int:pk>/chattingrooms",
        views.ChattingRoomViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "chattingrooms/<int:pk>",
        views.ChattingRoomViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
    ),
]
