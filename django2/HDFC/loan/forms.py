from django import forms


class EmpDetailsForms(forms.Form):
    emp_id=forms.IntegerField()
    emp_name=forms.CharField(max_length=10)
    emp_sal=forms.IntegerField()
    emp_city=forms.CharField(max_length=20)

