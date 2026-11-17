from django.http import HttpResponse

from .models import Player, Position


def home(request):
    return HttpResponse(
        f"<h1>Rugby Teams</h1><p>{Player.objects.count()} players, "
        f"{Position.objects.count()} positions.</p>"
    )
