from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    online = models.ForeignKey(
        "onlines.Online",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    offline = models.ForeignKey(
        "offlines.Offline",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    challenge = models.ForeignKey(
        "challenges.Challenge",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    textArea = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating} ⭐️"
