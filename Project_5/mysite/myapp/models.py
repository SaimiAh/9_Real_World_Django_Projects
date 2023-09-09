from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=200)
    carbs =  models.FloatField()
    protien = models.FloatField()
    fats = models.FloatField()
    calorie =  models.FloatField()

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)