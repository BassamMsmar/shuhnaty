from django.urls import path
from .views import driver_list, driver_details, add_driver, edit_driver, delete_driver

urlpatterns = [
    path('deivers/',driver_list, name='driver_list' ),
    path('deivers/details/<int:pk>',driver_details, name='driver_details' ),
    path('deivers/add',add_driver, name='add_driver' ),
    path('deivers/edit/<int:pk>',edit_driver, name='edit_driver' ),
    path('deivers/delete/<int:pk>',delete_driver, name='delete_driver' ),
]