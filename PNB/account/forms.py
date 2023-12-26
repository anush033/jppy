from .models import FormsfieldsModel
from django import forms


class AccountOpeningForm(forms.ModelForm):
    class Meta:
        model = FormsfieldsModel
        fields = "__all__"
