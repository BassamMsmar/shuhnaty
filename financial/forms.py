from django import forms
from .models import CatchReceipt


class AddCatch(forms.ModelForm):
    class Meta:
        model = CatchReceipt
        fields = '__all__'
        exclude = [
            'date',
            'accountant',
            ]
        
        

