from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Module, Student

PER_PAGE = 20


def home(request):
    return render(request, "myApp/home.html")


def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404(f"Student {student_id} not found!")

    return render(request, "myApp/student_detail.html", {"student": student})


def studentlist(request, page):
    students = Student.objects.all().order_by("lastName")
    paginator = Paginator(students, PER_PAGE)
    page_obj = paginator.get_page(page)
    # elided page range gives "1 2 ... 5 6 7 ... 12" style navigation
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(
        page_obj.number, on_each_side=1, on_ends=1
    )
    return render(request, "myApp/studentlist.html", {"page_obj": page_obj})


def modulelist(request, page):
    modules = Module.objects.all().order_by("code")
    paginator = Paginator(modules, PER_PAGE)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(
        page_obj.number, on_each_side=1, on_ends=1
    )
    return render(request, "myApp/modulelist.html", {"page_obj": page_obj})
