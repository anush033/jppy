from django.db import models

# Create your models here.
class ZaraModel(models.Model):
    brand_name = models.CharField(max_length=25)
    price = models.IntegerField()
    size = models.CharField(max_length=25)
