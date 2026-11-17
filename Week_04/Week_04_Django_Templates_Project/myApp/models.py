from django.db import models


class Module(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.code} {self.name}"


class Student(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    modules = models.ManyToManyField(Module, related_name="students", blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
