from django.db import models
from common.models import CommonModel

# Create your models here.


class Online(CommonModel):
    class TimeChoices(models.TextChoices):
        TIME20 = ("20MINS", "20MINS")
        TIME40 = ("40MINS", "40MINS")
        TIME60 = ("60MINS", "60MINS")

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
        choices=TimeChoices.choices,
    )

    subjects = models.ManyToManyField(
        "subjects.Subject",
        related_name="classes",
    )

    level = models.ForeignKey(
        "levels.Level",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "online_classes"

    def rating(onlineClass):
        count = onlineClass.reviews.count()
        if count == 0:
            return "No Review"
        else:
            total_rating = 0
            for review in onlineClass.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 1)
