from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=300)
    description = models.TextField()
    image = models.CharField(max_length=300)