from django.contrib import admin
from django.contrib import admin
from .models import FormsfieldsModel
# Register your models here.
class AccountOpeningAdmin(admin.ModelAdmin):
    list_display = ['Name','Age','Email','count','Contact']

admin.site.register(FormsfieldsModel,AccountOpeningAdmin)
# Register your models here.
