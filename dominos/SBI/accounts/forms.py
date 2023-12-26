from .models import AccountOpeningModel
from django import forms

class AccountOpeningForm(forms.ModelForm):
    class Meta:
        model = AccountOpeningModel
        fields = "__all__"