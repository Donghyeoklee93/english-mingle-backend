from django.urls import path
from . import views

urlpatterns = [
    path("", views.Offlines.as_view()),
    path("<int:pk>", views.OfflineDetail.as_view()),
    # path(
    #     "",
    #     views.OfflineViewSet.as_view(
    #         {
    #             "get": "list",
    #             "post": "create",
    #         }
    #     ),
    # ),
    # path(
    #     "<int:pk>",
    #     views.OfflineViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #             "put": "partial_update",
    #             "delete": "destroy",
    #         },
    #     ),
    # ),
]
