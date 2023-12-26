from django.contrib import admin
from .models import datatable
class datadmin(admin.ModelAdmin):
    list_display=['Name','age','city']
admin.site.register(datatable,datadmin)

# Register your models here.
