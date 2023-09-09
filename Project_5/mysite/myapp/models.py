from django.db import models

class Food(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=200)
    carbs =  models.FloatField()
    protien = models.FloatField()
    fats = models.FloatField()
    calorie =  models.FloatField()