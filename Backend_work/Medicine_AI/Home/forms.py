from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    Username = forms.CharField(max_length=100)
    First_name = forms.CharField(max_length=100)
    Last_name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    password_1 = forms.CharField(max_length=10)
    password_2 = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password_1','password_2']