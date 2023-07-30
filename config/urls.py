from django.contrib import admin
from django.urls import path, include

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/levels/", include("levels.urls")),
    path("api/v1/subjects/", include("subjects.urls")),
    path("api/v1/onlines/", include("onlines.urls")),
    path("api/v1/offlines/", include("offlines.urls")),
    path("api/v1/challenges/", include("challenges.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/messengers/", include("messengers.urls")),
]
