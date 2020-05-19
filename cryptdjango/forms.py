
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=100, help_text='Last Name')
    lastname = forms.CharField(max_length=100, help_text='Last Name')
    country = forms.CharField(max_length=100, help_text='Country of residence')
    title = forms.CharField(max_length=100, help_text='Mr/Mrs/Master/miss ')
    phonenumber = forms.CharField(max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')



    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2','country' )