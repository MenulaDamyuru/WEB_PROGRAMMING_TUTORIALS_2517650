from django.contrib import admin
from .models import Position, RugbyPlayer


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "specialist")
    list_filter = ("specialist",)
    search_fields = ("name",)


@admin.register(RugbyPlayer)
class RugbyPlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team")
    list_filter = ("team", "positions")
    search_fields = ("first_name", "last_name", "team")
    filter_horizontal = ("positions",)
