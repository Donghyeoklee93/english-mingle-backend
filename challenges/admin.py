from django.contrib import admin
from .models import Challenge


@admin.action(description="Set all price to zero")
def reset_price(model_admin, request, challenges):
    for challenge in challenges:
        challenge.price = 0
        challenge.save()


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    actions = (reset_price,)

    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
        "rating",
    )

    list_filter = (
        "subjects",
        "level",
    )

    search_fields = [
        "name",
        "^tutor__username",
    ]
