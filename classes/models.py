from django.db import models
from common.models import CommonModel

# Create your models here.


class Class(CommonModel):
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
        "classes.Subject",
        related_name="classes",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Classes"


class Subject(CommonModel):

    """Subject Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
