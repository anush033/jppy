from django.contrib import admin
from .models import LoanDetailsModel
# Register your models here.

class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ['loanid','loan_acc','name','age','city']

admin.site.register(LoanDetailsModel,LoanDetailsAdmin)