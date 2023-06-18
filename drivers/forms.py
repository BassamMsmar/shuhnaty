from django import forms
from .models import DriverModel

class AddDriverForm(forms.ModelForm):
    class Meta:
        model = DriverModel
        fields = ("__all__")