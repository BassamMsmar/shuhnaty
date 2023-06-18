from django.db import models

# Create your models here.
# Create your models here.

class CompanyModel(models.Model):
    company_name = models.CharField(max_length=225,  help_text='اسم الشركة')
    company_id = models.BigAutoField(primary_key=True)
    company_city = models.CharField(max_length=225,  default='Dammam',help_text='مقر الشركة')
    charging_area = models.CharField( max_length=225, default='Jeddah', help_text='منطقة الشحن ')
    

    def __str__(self):
        return self.company_name
