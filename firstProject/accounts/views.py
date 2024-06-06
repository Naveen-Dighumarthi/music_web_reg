# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import SignupForm, LoginForm
from musicbeat.models import Song
def home(request):
     song=Song.objects.all()
     return render(request,'index.html',{'song':song})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # Redirect to the login page after successful signup
            return redirect('login')  # Assuming you have a URL name 'login' for your login page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('index')  # Replace 'index' with the name of your home page URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
                
    return render(request, 'login.html', {'form': form})
