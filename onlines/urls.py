from django.urls import path
from . import views

urlpatterns = [
    path("", views.Onlines.as_view()),
    path("<int:pk>", views.OnlinesDetail.as_view()),
    # path(
    #     "",
    #     views.OnlineViewSet.as_view(
    #         {
    #             "get": "list",
    #             "post": "create",
    #         }
    #     ),
    # ),
    # path(
    #     "<int:pk>",
    #     views.OnlineViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #             "put": "partial_update",
    #             "delete": "destroy",
    #         },
    #     ),
    # ),
]
