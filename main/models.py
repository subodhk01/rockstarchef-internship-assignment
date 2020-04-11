from django.db import models

RATING = [ (1,1), (2,2), (3,3), (4,4), (5,5) ]

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    time_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, choices=RATING)

