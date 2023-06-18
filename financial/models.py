from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget

from accounts.forms import User
from companies.models import CompanyModel
from drivers.models import DriverModel

# Create your models here.
class CatchReceipt(models.Model):
    catchReceipt_id= models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE, null=True )
    source =  models.CharField(max_length=225,  default='جدة' , help_text=' المصدر' , blank=True )
    destination =  models.CharField(max_length=225,  default='الرياض' ,  help_text=' الوجهة', blank=True )
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True , blank=True )
    date = models.DateTimeField(default=timezone.now, help_text=' التاريخ' , blank=True )
    amount =  models.CharField(max_length=225,  help_text=' الاجرة'  )
    overnight =  models.CharField(max_length=225,  default='0' ,  help_text=' المبات'  )
    return_fare =  models.CharField(max_length=225,  default='0' ,  help_text=' اجرة رجعة' )
    deduction =  models.CharField(max_length=225,  default='0' ,  help_text='خصم' )
    total_amount =  models.CharField(max_length=225,  default='0' ,  help_text='المجموع', null=True, blank=True )
    policy_number =  models.CharField(max_length=225,  default='' , help_text=' رقم البوليصة' , blank=True )
    notice_number =  models.CharField(max_length=225,  default='' , help_text=' رقم الاشعار' , blank=True )
    Shipment_id =  models.CharField(max_length=225,  default='' , help_text=' رقم الشحن' , blank=True )
    delegate =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, help_text=' المندوب ')
    accountant =  models.CharField(max_length=225, null=True,help_text=' المحاسب ' )

    Truck_Reefers = 'تريلا براد'
    Truck_Flatbed  = 'سطحة'
    Truck_high_sides = 'جوانب عالي'
    Truck_Curtainsider = 'ستارة'
    lory_Flatbed= 'لوري عادي'
    lory_Reefers= 'لوري براد'
    dinah_Flatbed= 'يدنة عادي'
    dinah_Reefers= 'دينة براد'
    
   
    Vehicle = [
        (Truck_Reefers, 'تريلا براد'),
        (Truck_Flatbed, 'سطحة'),
        (Truck_high_sides, 'جوانب عالي'),
        (Truck_Curtainsider, 'ستارة'),
        (lory_Flatbed, 'لوري عادي'),
        (lory_Reefers, 'يدنة عادي'),
        (dinah_Flatbed, 'يدنة عادي'),
        (dinah_Reefers, 'دينة براد'),
    ]
    Vehicle_Type = models.CharField( choices=Vehicle, default=Truck_Flatbed,
        max_length=30, help_text='نوع السيارة(سطحة - جوانب) ....',  null=True, blank=True )
    branch = models.CharField(max_length=225,  default='المركز الرئيسي' , help_text=' الفرع' , blank=True, null=True, )
   
    payment_method = models.CharField( max_length=225,  default='نقداً' , help_text=' طريقة الدفع' , blank=True, null=True, )




    
    def __str__(self):
        return str(self.catchReceipt_id)
