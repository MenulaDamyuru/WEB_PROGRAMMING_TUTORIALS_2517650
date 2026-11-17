from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=60, unique=True)
    specialist = models.BooleanField(default=False)

    def __str__(self):
        if self.specialist:
            return f"{self.name} (Specialist)"
        return self.name


class RugbyPlayer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    positions = models.ManyToManyField(Position, blank=True, related_name="players")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["team", "last_name", "first_name"]
