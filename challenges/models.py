from django.db import models
from common.models import CommonModel


class Challenge(CommonModel):
    class ChallengeChoices(models.TextChoices):
        LVEC = ("LVEC", "LVEC")
        UEEC = ("UEEC", "UEEC")
        EDEC = ("EDEC", "EDEC")

    name = models.CharField(
        max_length=150,
        verbose_name="class name",
        help_text="class name only",
    )

    tutor = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    price = models.PositiveIntegerField()
    description = models.TextField()

    kind = models.CharField(
        max_length=20,
        choices=ChallengeChoices.choices,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()

    subjects = models.ManyToManyField(
        "classes.Subject",
    )

    def __str__(self) -> str:
        return self.name
