import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from django.forms import ModelForm
from .models import CatchReceipt
from django.contrib.admin.widgets import AdminDateWidget



class DateInput(forms.DateInput):

    input_type = 'date'
    

class CatchFielter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte', widget=DateInput, )   
    end_date = DateFilter(field_name="date", lookup_expr='lte', widget=DateInput,)
    class Meta:
        model = CatchReceipt
        fields = (
            'start_date', 'end_date', 'company', 'delegate', 'accountant',
        )
