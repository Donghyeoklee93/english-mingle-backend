from django.contrib import admin
from .models import Event

# Register your models here.


@admin.action(description="Set all price to zero")
def reset_price(model_admin, request, events):
    for event in events:
        event.price = 0
        event.save()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    actions = (reset_price,)

    list_display = [
        "name",
        "tutor",
        "price",
        # "description",
        "address",
        "rating",
    ]

    list_filter = [
        "price",
        "level",
    ]

    search_fields = [
        "name",
        "^tutor__username",
    ]
