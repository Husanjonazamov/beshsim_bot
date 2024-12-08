# forms.py
from django import forms
from .models import PhoneNumber, Category, Sim

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'category', 'company']
