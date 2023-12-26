from django.db import models
class LoandetailsModel(models.Model):
    loan_id=models.IntegerField()
    loan_acc_no=models.IntegerField()
    loanholdername=models.CharField(max_length=25)
    loan_amount=models.IntegerField()


# Create your models here.
