from django.shortcuts import render, redirect
from django.urls import is_valid_path
from .models import Users
from .forms import CustomUserChangeForm

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
def detail(request, pk):
    d = Users.objects.get(pk=pk)
    context ={
        'd' : d,
    }
    return render(request,'accounts/detail.html', context)
def update (request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form' : form
    }
    return render(request, 'accounts/update.html', context)