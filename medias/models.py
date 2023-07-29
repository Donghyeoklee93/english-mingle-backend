from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    classes = models.ForeignKey(
        "classes.Class",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    event = models.ForeignKey(
        "events.Event",
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
    event = models.OneToOneField(
        "events.Event",
        on_delete=models.CASCADE,
        related_name="video",
    )

    def __str__(self) -> str:
        return "Video File"
