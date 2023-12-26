from django.contrib import admin
from .models import LoandetailsModel

class EmpdetailsAdmin(admin.ModelAdmin):
    list_display=['loan_id','loanholdername','loan_amount']
admin.site.register(LoandetailsModel,EmpdetailsAdmin)
