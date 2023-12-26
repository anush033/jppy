from django import forms
class pizzafeedbackforms(forms.Form):
    crust_quality=forms.CharField(max_length=25)
    servicing=forms.CharField(max_length=25)