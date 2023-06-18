from django.shortcuts import render, redirect, get_object_or_404
from .models import DriverModel
from .forms import AddDriverForm
from  django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def driver_list(request):
    drivers = DriverModel.objects.all()
    return render(request, 'drivers/driver-list.html',{'drivers':drivers})
@login_required(login_url='login')
def driver_details(request, pk):
    drivers = get_object_or_404(DriverModel, pk=pk)
    return render(request, 'drivers/driver_details.html',{'drivers':drivers})
@login_required(login_url='login')
def add_driver(request):
    if request.method == 'POST':
        driver_form = AddDriverForm(request.POST, request.FILES)
        if driver_form.is_valid():
            driver_form.save()
            return redirect('driver_list')
    else:
        driver_form = AddDriverForm()

    return render(request, 'drivers/driver-add_edit.html',{'driver_form':driver_form})

@login_required(login_url='login')
def edit_driver(request, pk):
    driver = get_object_or_404(DriverModel, pk=pk)
    if request.method == 'POST':
        driver_form = AddDriverForm(request.POST, instance=driver)
        if driver_form.is_valid():
            driver_form.save()
            return redirect('driver_list')
    else:
        driver_form = AddDriverForm(instance=driver)

    return render(request, 'drivers/driver-add_edit.html',{'driver_form':driver_form})
@login_required(login_url='login')
def delete_driver(request, pk):
    driver = get_object_or_404(DriverModel, pk=pk)
    driver.delete()
    return redirect('driver_list')
    

    
    