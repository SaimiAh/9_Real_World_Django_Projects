from django.db import models


class item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
