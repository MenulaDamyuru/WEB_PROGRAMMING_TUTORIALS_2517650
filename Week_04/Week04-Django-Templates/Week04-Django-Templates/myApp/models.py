from django.db import models


class Module(models.Model):
    """A university module that students can be enrolled on."""

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)


    class Meta:
        ordering = ["code"]


class Student(models.Model):
    """A student enrolled on zero or more modules."""

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    enrolmentDate = models.DateTimeField()
    # Many students can be enrolled on many modules.
    modules = models.ManyToManyField("Module", blank=True)


    class Meta:
        ordering = ["lastName", "firstName"]
