from django.test import TestCase
from django.urls import reverse

from .models import Module, Student


class StaticsAndPaginationTests(TestCase):
    """Week 05 - __str__, media configuration, statics and pagination."""

    @classmethod
    def setUpTestData(cls):
        cls.web = Module.objects.create(code="MOD002619", name="Web Programming")
        for i in range(45):
            student = Student.objects.create(
                firstName=f"Student{i:02d}", lastName="Test", age=20 + (i % 5),
                email=f"s{i}@student.aru.ac.uk",
                enrolmentDate="2024-09-01T09:00:00Z",
            )
            if i % 2 == 0:
                student.modules.add(cls.web)

    def test_str_methods(self):
        student = Student.objects.first()
        self.assertEqual(str(student), student.firstName.capitalize() + ", TEST")
        self.assertEqual(str(self.web), "MOD002619 Web Programming")

    def test_first_page_has_twenty_students(self):
        response = self.client.get(reverse("myApp:studentlist", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["page_obj"]), 20)
        self.assertEqual(response.context["page_obj"].paginator.num_pages, 3)

    def test_last_page_has_remainder(self):
        response = self.client.get(reverse("myApp:studentlist", args=[3]))
        self.assertEqual(len(response.context["page_obj"]), 5)

    def test_page_out_of_range_is_clamped(self):
        response = self.client.get(reverse("myApp:studentlist", args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page_obj"].number, 3)

    def test_studentlist_uses_bootstrap_and_shows_str(self):
        response = self.client.get(reverse("myApp:studentlist", args=[1]))
        self.assertContains(response, "bootstrap.min.css")
        self.assertContains(response, "table-striped")

    def test_modulelist(self):
        response = self.client.get(reverse("myApp:modulelist", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MOD002619")

    def test_detail_without_image_does_not_error(self):
        student = Student.objects.filter(image="").first()
        response = self.client.get(reverse("myApp:student_detail", args=[student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photograph on file.")

    def test_media_settings(self):
        from django.conf import settings
        self.assertEqual(settings.MEDIA_URL, "/media/")
