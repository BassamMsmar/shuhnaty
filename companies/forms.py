from django import forms
from .models import CompanyModel


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = ("__all__")