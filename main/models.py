from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}"