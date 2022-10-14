from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    users = Users.objects.all()
    context = {
        "users" : users
    }

    return render(request, 'accounts/index.html', context)

from .forms import CustomUserCreationForm

def signup(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    
    context = {
        "form" : form
    }

    return render(request, 'accounts/signup.html', context)