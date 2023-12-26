from .models import LoandetailsModel
from django import forms


class Loanform(forms.ModelForm):
    class Meta:
        model = LoandetailsModel
        fields = "__all__"