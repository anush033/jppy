from django.db import models
class datatable(models.Model):
    Name=models.CharField(max_length=25)
    age=models.BigIntegerField()
    city=models.CharField(max_length=25)


# Create your models here.
