from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    amount = models.IntegerField()
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, related_name='categories')
