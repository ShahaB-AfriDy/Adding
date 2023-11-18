# forms.py
from django import forms

class AddNumbersForm(forms.Form):
    num1 = forms.IntegerField(label='')
    num2 = forms.IntegerField(label='')
