from django import forms
from .models import datatable
class formdata(forms.ModelForm):
    class Meta:
        model=datatable
        fields="__all__"



