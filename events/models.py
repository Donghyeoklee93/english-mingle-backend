from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="student name",
        help_text="student's name only",
    )

    tutor = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
