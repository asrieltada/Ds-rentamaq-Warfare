from django import forms
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'password']

class updateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
