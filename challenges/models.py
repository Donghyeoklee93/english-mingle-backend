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

    subjects = models.ManyToManyField(
        "subjects.Subject",
    )

    level = models.ForeignKey(
        "levels.Level",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # start = models.DateTimeField()
    # end = models.DateTimeField()

    start = models.TimeField()
    end = models.TimeField()

    def __str__(self) -> str:
        return self.name

    def rating(challenges):
        count = challenges.reviews.count()
        if count == 0:
            return "No Review"
        else:
            total_rating = 0
            for review in challenges.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 1)
