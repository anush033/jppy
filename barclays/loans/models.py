from django.db import models

# Create your models here.

class LoanDetailsModel(models.Model):
    loanid = models.IntegerField(primary_key=True)
    loan_acc = models.IntegerField()
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    city = models.CharField(max_length=25)