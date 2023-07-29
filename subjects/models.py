from django.db import models
from common.models import CommonModel


# Create your models here.
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
