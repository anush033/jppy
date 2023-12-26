from django.contrib import admin
from .models import ZaraModel


class ZaraModelAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'price', 'size']


admin.site.register(ZaraModel, ZaraModelAdmin)
# Register your models here.
