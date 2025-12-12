from django.db import models

# Create your models here.

class Event(models.Model):

    LOCATION_CHOICES = [
        ("Ogden", "ogden"),
        ("Salt Lake City", "slc"),
        ("Logan", "logan"),
        ("Park City", "park city"),
        ("St. George", "st. george"),
    ]


    title = models.CharField(max_length=150)
    description = models.TextField()
    location =  models.CharField(choices= LOCATION_CHOICES)
    date = models.DateTimeField()