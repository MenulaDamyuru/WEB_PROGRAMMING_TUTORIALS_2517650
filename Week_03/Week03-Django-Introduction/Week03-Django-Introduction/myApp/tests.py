from django.test import TestCase
from django.urls import reverse

from .models import Module, Student


class ModelTests(TestCase):
    """Week 03 - the data layer works and the relationships behave."""

    def setUp(self):
        self.web = Module.objects.create(code="MOD002619", name="Web Programming")
        self.ipp = Module.objects.create(code="MOD003212", name="Introduction to Programming")
        self.student = Student.objects.create(
            firstName="Connie", lastName="James", age=20,
            email="connie@student.aru.ac.uk",
            enrolmentDate="2024-09-01T09:00:00Z",
        )
        self.student.modules.add(self.web, self.ipp)

    def test_module_fields(self):
        """Week 03 models have no __str__ yet - assert on the stored fields."""
        self.assertEqual(self.web.code, "MOD002619")
        self.assertEqual(self.web.name, "Web Programming")

    def test_student_has_two_modules(self):
        self.assertEqual(self.student.modules.count(), 2)
        self.assertIn("Web Programming", [m.name for m in self.student.modules.all()])

    def test_home_page_responds(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My University")
