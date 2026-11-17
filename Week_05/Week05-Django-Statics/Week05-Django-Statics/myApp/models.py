from django.db import models


class Module(models.Model):
    """A university module that students can be enrolled on."""

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} {self.name}"


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

    # Only the path is stored in the database; the file is written to
    # <BASE_DIR>/images/ because MEDIA_ROOT is BASE_DIR in settings.py
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        # Used by the admin site and anywhere an object is printed
        return self.firstName.capitalize() + ", " + self.lastName.upper()


    class Meta:
        ordering = ["lastName", "firstName"]
