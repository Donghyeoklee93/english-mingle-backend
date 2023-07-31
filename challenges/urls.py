from django.urls import path
from . import views

urlpatterns = [
    path("", views.Challenges.as_view()),
    path("<int:pk>", views.ChallengeDetail.as_view()),
    # path(
    #     "",
    #     views.ChallengeViewSet.as_view(
    #         {
    #             "get": "list",
    #             "post": "create",
    #         }
    #     ),
    # ),
    # path(
    #     "<int:pk>",
    #     views.ChallengeViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #             "put": "partial_update",
    #             "delete": "destroy",
    #         },
    #     ),
    # ),
]
