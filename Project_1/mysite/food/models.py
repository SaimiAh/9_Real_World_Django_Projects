from django.db import models


class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")
