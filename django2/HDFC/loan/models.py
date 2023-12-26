from django.db import models


# Create your models here.

class PersonalDetailsModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    contact = models.BigIntegerField()

class LoanDetailModel(models.Model):
    loan_acc=models.IntegerField()
    loan_holder=models.CharField(max_length=25)
    loan_amount=models.IntegerField()
