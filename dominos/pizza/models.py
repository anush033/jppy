from django.db import models


class PizzaModel(models.Model):
    pizza_name=models.CharField(max_length=25)
    xtra_cheese=models.CharField(max_length=10)
    veg_nonveg=models.CharField(max_length=10)
    pizza_base=models.CharField(max_length=10)




