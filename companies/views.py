from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib.auth.decorators import login_required

from .models import CompanyModel

from .forms import AddCompanyForm

# Create your views here.

@login_required(login_url='login')
def company_list(request):
    companies = CompanyModel.objects.all()
    return render (request, 'companies/company_list.html',{'companies':companies})
@login_required(login_url='login')
def company_details(request, pk):
    companies = get_object_or_404(CompanyModel, pk=pk)
    return render (request, 'companies/company_detials.html',{'companies':companies})

@login_required(login_url='login')
def company_delete(request, pk):
    companies = CompanyModel.objects.get(pk=pk)
    companies.delete()
    return redirect('company_list')

@login_required(login_url='login')
def add_company(request):
    if request.method == 'POST':
        company_form = AddCompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_list')
    
    else:
        company_form = AddCompanyForm()
    return render(request, 'companies/company-add_edit.html',{'company_form':company_form})

@login_required(login_url='login')
def edit_company(request, pk):
    companies = get_object_or_404(CompanyModel, pk=pk)
    if request.method == 'POST':
        company_form = AddCompanyForm(request.POST, instance=companies)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_list')
    
    else:
        company_form = AddCompanyForm(instance=companies)
    return render(request, 'companies/company-add_edit.html',{'company_form':company_form})