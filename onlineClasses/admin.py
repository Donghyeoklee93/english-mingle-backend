from django.contrib import admin
from .models import OnlineClass, Subject


@admin.action(description="Set all price to zero")
def reset_price(model_admin, request, onlineClasses):
    for onlineClass in onlineClasses:
        onlineClass.price = 0
        onlineClass.save()


@admin.register(OnlineClass)
class ClassAdmin(admin.ModelAdmin):
    actions = (reset_price,)

    list_display = (
        "name",
        "price",
        "kind",
        "tutor",
        "rating",
    )

    list_filter = (
        "name",
        "price",
        "kind",
        "tutor",
        "subject",
        "created_at",
        "updated_at",
        "level",
    )

    search_fields = [
        "name",
        "^tutor__username",
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
