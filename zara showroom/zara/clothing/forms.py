from django import forms
from .models import ZaraModel


class ZaraForms(forms.ModelForm):
    class Meta:
        model = ZaraModel
        fields = "__all__"
