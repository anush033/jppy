from django.db import models
from django.db import models

class beveModel(models.Model):
    beve_name=models.CharField(max_length=25)
    size=models.CharField(max_length=10)
    ice=models.CharField(max_length=10)


# Create your models here.
