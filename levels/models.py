from django.db import models
from common.models import CommonModel


class Level(CommonModel):

    """Room or Experience Category"""

    class LevelKindChoices(models.TextChoices):
        BEGINNER = "BEGINNER", "BEGINNER"
        INTERMIDATE = "INTERMIDATE", "INTERMIDATE"
        ADVANCE = "ADVANCE", "ADVANCE"

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(
        max_length=15,
        choices=LevelKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"
