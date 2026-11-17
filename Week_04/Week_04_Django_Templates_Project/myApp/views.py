from django.http import Http404
from django.shortcuts import render
from .models import Student


def home(request):
    # ORM query: retrieve all students from the database.
    students = Student.objects.all().order_by("firstName", "lastName")
    return render(request, "home.html", {"students": students})


def student_detail(request, student_id):
    # ORM query: retrieve one student using the URL parameter.
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404(f"Student {student_id} not found!")

    return render(request, "student_detail.html", {"student": student})
