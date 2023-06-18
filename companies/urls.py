from django.urls import path
from .views import  company_list, add_company, edit_company, company_details, company_delete

urlpatterns = [
    path('companies/',company_list, name='company_list' ),
    path('companies/add/',add_company, name='add_company' ),
    path('companies/edit/<int:pk>',edit_company, name='edit_company' ),
    path('companies/detials/<int:pk>',company_details, name='company_details' ),
    path('companie/delete/<int:pk>',company_delete, name='company_delete' ),

 
]