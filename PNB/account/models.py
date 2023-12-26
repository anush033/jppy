from django.db import models


class FormsfieldsModel(models.Model):
    acc_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=25)

    Age = models.IntegerField()
    Email = models.EmailField()
    Contact = models.BigIntegerField()
    Date = models.DateField()
    count = models.IntegerField()
