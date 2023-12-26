from django.contrib import admin
from .models import LoanDetailModel, PersonalDetailsModel


# Register your models here.

class LoanDetailAdmin(admin.ModelAdmin):
    list_display = ['loan_acc', 'loan_holder', "loan_amount"]


class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "contact"]


admin.site.register(PersonalDetailsModel, PersonalDetailsAdmin)
admin.site.register(LoanDetailModel, LoanDetailAdmin)
