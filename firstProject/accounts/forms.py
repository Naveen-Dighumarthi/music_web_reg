# Inside myapp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class LoginForm(AuthenticationForm):
    # You can customize the login form here if needed
    pass        
       
