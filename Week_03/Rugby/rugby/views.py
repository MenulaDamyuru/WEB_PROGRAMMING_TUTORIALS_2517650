from django.shortcuts import render
from .models import RugbyPlayer


def home(request):
    players = RugbyPlayer.objects.prefetch_related("positions").all()
    return render(request, "rugby/home.html", {"players": players})
