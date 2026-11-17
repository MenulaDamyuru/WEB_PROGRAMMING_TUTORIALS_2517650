from django.http import Http404
from django.shortcuts import render

from .models import Student


def home(request):
    """List every student with a link to their detail page."""
    # ORM query: every Student row, already ordered by last name / first name
    students = Student.objects.all()
    return render(request, "myApp/home.html", {"students": students})


def student_detail(request, student_id):
    try:
        # Single object query - raises DoesNotExist if there is no match
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404(f"Student {student_id} not found!")

    return render(request, "myApp/student_detail.html", {"student": student})
