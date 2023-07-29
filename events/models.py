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

    subject = models.ManyToManyField(
        "onlineClasses.Subject",
    )

    level = models.ForeignKey(
        "levels.Level",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    def rating(events):
        count = events.reviews.count()
        if count == 0:
            return "No Review"
        else:
            total_rating = 0
            for review in events.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 1)
