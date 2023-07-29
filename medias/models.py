from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    online = models.ForeignKey(
        "onlines.Online",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    Offline = models.ForeignKey(
        "offlines.Offline",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    challenge = models.ForeignKey(
        "challenges.Challenge",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):
    file = models.URLField()
    offline = models.OneToOneField(
        "offlines.Offline",
        on_delete=models.CASCADE,
        related_name="video",
    )

    def __str__(self) -> str:
        return "Video File"
