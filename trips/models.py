from django.db import models

# Create your models here.
class Trip(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    crew_needed = models.IntegerField()

    def __str__(self):
        return self.title