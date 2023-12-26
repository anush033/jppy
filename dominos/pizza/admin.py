from django.contrib import admin
from .models import PizzaModel
class PizzaAdmin(admin.ModelAdmin):
    list_display=['pizza_name','xtra_cheese','veg_nonveg']

admin.site.register(PizzaModel,PizzaAdmin)
# Register your models here.
