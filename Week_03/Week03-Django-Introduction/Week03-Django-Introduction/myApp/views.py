from django.http import HttpResponse

from .models import Module, Student


def home(request):
    """Simple check that the project, app and database are wired up."""
    return HttpResponse(
        "<h1>My University</h1>"
        "<p>Week 03 - Django introduction.</p>"
        f"<p>{Student.objects.count()} students and "
        f"{Module.objects.count()} modules are in the database.</p>"
        "<p><a href='/admin/'>Go to the admin site</a></p>"
    )
