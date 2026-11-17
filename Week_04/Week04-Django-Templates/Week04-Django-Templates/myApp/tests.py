from django.test import TestCase
from django.urls import reverse

from .models import Module, Student


class TemplateTests(TestCase):
    """Week 04 - ORM queries, URL paths, templates and inheritance."""

    @classmethod
    def setUpTestData(cls):
        cls.web = Module.objects.create(code="MOD002619", name="Web Programming")
        cls.student = Student.objects.create(
            firstName="connie", lastName="James", age=20,
            email="connie@student.aru.ac.uk",
            enrolmentDate="2024-09-01T09:00:00Z",
        )
        cls.student.modules.add(cls.web)

    def test_home_lists_students(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        # filters applied by the template: capfirst + upper
        self.assertContains(response, "Connie JAMES")
        self.assertTemplateUsed(response, "myApp/home.html")
        self.assertTemplateUsed(response, "myApp/base.html")

    def test_home_links_to_detail(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, f"/myApp/{self.student.id}/")

    def test_student_detail(self):
        response = self.client.get(reverse("student_detail", args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Web Programming")
        self.assertContains(response, "20")

    def test_missing_student_is_404(self):
        response = self.client.get(reverse("student_detail", args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_unknown_url_is_404(self):
        response = self.client.get("/bob/")
        self.assertEqual(response.status_code, 404)

    def test_orm_queries(self):
        self.assertEqual(Student.objects.count(), 1)
        student = Student.objects.get(id=self.student.id)
        self.assertEqual(student.modules.all()[0].code, "MOD002619")
        self.assertEqual(Student.objects.filter(age__gte=18).count(), 1)
