from django.contrib import admin
from .models import Offline

# Register your models here.


@admin.action(description="Set all price to zero")
def reset_price(model_admin, request, offlines):
    for offline in offlines:
        offline.price = 0
        offline.save()


@admin.register(Offline)
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
