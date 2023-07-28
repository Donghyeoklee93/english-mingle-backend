from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="student name",
        help_text="student's name only",
    )
    tutor = models.CharField(
        max_length=150,
        verbose_name="tutor name",
        help_text="tutor's name only",
    )
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
