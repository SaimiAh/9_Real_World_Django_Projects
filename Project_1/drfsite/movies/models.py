from django.db import models

class MovieData(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
