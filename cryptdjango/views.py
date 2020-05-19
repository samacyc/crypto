from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import *
#Admin101$$$

def hp(request):
    return render(request, 'cryptyy/hp.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return redirect('login')
        else:
            return redirect('dashboard')
    context = {}
    return render(request, 'cryptyy/login.html', context)



def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.firstname = form.cleaned_data.get('firstname')
        user.profile.lastname = form.cleaned_data.get('lastname')
        user.profile.email = form.cleaned_data.get('email')

        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'cryptyy/signup.html', {'form': form})

def dashboard(request):
    return render(request, 'cryptyy/dashboard.html') 