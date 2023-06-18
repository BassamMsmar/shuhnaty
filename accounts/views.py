from django.shortcuts import render
from django.contrib.auth import get_user_model

from .forms import SingUpForm

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = SingUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'registration/signup-successful.html', {'user_form':user_form})
    else:
        user_form = SingUpForm()

    return render(request, 'registration/signup.html', {'user_form':user_form})

def accounts_list(request):
    users = User.objects.all()
 
    return render(request, 'registration/accounts_list.html', {'users':users})

