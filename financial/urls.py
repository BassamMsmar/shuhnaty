from django.urls import path
from . import views



urlpatterns = [
    path('financial/catch/',views.catch_receipt_list, name='catch_receipt_list' ),
    path('financial/catch/details/<int:pk>',views.catch_receipt_details, name='catch_receipt_details' ),
    path('financial/catch/add/',views.add_catch_receipt, name='add_catch_receipt' ),
    path('financial/catch/edit/<int:pk>',views.edit_catch_receipt, name='edit_catch_receipt' ),
    path('financial/catch/delete/<int:pk>',views.delete_catch_receipt, name='delete_catch_receipt' ),
    path('financial/check_list',views.check_list, name='check_list' ),




]
