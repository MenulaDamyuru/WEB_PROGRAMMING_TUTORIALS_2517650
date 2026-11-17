from django.db import models


class Position(models.Model):
    """A rugby position. Specialist positions are restricted for safety."""

    name = models.CharField(max_length=50, unique=True)
    specialist = models.BooleanField(
        default=False,
        help_text="Only players allocated to this position may play it.",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Player(models.Model):
    """A rugby player, who may be able to play several positions."""

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    squadNumber = models.IntegerField(unique=True)
    positions = models.ManyToManyField("Position", blank=True)

    class Meta:
        ordering = ["squadNumber"]

    def __str__(self):
        return f"#{self.squadNumber} {self.firstName} {self.lastName}"
