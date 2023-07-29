from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chat_rooms",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Messenger(CommonModel):

    """Messenger Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messengers",
    )
    room = models.ForeignKey(
        "messengers.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messengers",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
