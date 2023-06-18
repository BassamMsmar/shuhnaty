from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



User = get_user_model()

class SingUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='احرف انجليزية فقط ولا يحتوي على مسافات')
    number_phone = forms.CharField(max_length=16, required=False, help_text='966 5xxx xxxx xx')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = (
            'username', 
            'password1',
            'password2',
            'first_name',
            'last_name',
            'number_phone',
            )

