from django.contrib import admin
from .models import beveModel
class BeveAdmin(admin.ModelAdmin):
    list_display=['beve_name','size','ice']

admin.site.register(beveModel,BeveAdmin)
# Register your models here.
