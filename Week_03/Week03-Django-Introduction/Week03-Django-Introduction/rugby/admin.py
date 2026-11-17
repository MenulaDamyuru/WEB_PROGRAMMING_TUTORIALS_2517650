from django.contrib import admin

from .models import Player, Position

admin.site.register(Position)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("squadNumber", "firstName", "lastName")
    list_filter = ("positions",)
    search_fields = ("firstName", "lastName")
    filter_horizontal = ("positions",)
