from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        CLASS = "CLASS", "CLASS"
        EVENT = "EVENT", "EVENT"
        CHALLENGE = "CHALLENGE", "CHALLENGE"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    onlineclass = models.ForeignKey(
        "onlineClasses.Onlineclass",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    event = models.ForeignKey(
        "events.Event",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )
    challenge = models.ForeignKey(
        "challenges.Challenge",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    time_from = models.DateField(
        null=True,
        blank=True,
    )
    time_to = models.DateField(
        null=True,
        blank=True,
    )
    event_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    # guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for: {self.user}"
