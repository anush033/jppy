from django import forms
from .models import LoanDetailsModel

class LoanDetailsForm(forms.ModelForm):
    class Meta:
        model=LoanDetailsModel
        fields = "__all__"