from django.db import models

# Create your models here.


class DriverModel(models.Model):
    driver_id = models.BigAutoField(primary_key=True)
    driver_name = models.CharField(max_length=225,  help_text='اسم السائق',  null=True, blank=True)
    Saudi_Arabia = 'Saudi'
    YEMEN = 'Yemeni'
    Syria = 'Syrian'
    Egypt = 'Egypt'
    Afghanistan = 'Afghanistan'
    Pakistan = 'Pakistani'
    Jordan = 'Jordanian'
    India = 'Indian'
    Other = 'other'
    countrys = [
        (Saudi_Arabia, 'Saudi'),
        (YEMEN, 'Yemeni'),
        (Syria, 'Syrian'),
        (Egypt, 'Egypt'),
        (Afghanistan, 'Afghanistan'),
        (Pakistan, 'Pakistani'),
        (Jordan, 'Jordanian'),
        (India, 'Indian'),
        (Other, 'other')
    ]
    driver_nationality = models.CharField(
        max_length=20, choices=countrys, default=Other,  help_text='جنسية السائق',  null=True, blank=True)
    driver_phone_number = models.CharField(
        max_length=16, help_text='رقم هاتف السائق ',  null=True, blank=True)
    Identification_Number = models.CharField(
        max_length=10,  help_text='رقم الهوية/الاقامة',  null=True, blank=True)
    truck_plate_number = models.CharField(
        max_length=8,  help_text='رقم لوحة الشاحنة',  null=True, blank=True)
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
        max_length=30, help_text='نوع السيارة(سطحة - جوانب) ....',  null=True, blank=True)
    Sequence_Number = models.CharField(
        max_length=30, help_text='الرقم التسلسلي من الاستمارة',  null=True, blank=True)
    Owner_car_id_number = models.CharField(
        max_length=10,  help_text='رقم هوية مالك السيارة',  null=True, blank=True)
    # Identification_photo = models.ImageField(
    #     upload_to='driver/', null=True, help_text='صورة الهوية/الاقامة ')
    # license_photo = models.ImageField(upload_to='driver/', null=True, help_text=' صورة رخصة القيادة')
    # Sequence_image = models.ImageField(upload_to='driver/', null=True, help_text=' صورة من استمارة السيارة')
    # car_picture = models.ImageField(upload_to='driver/', null=True, help_text=' صورة جانبية او امامية للسيارة')

    def __str__(self):
        return self.driver_name
