from django.forms import ModelForm, fields
from django import forms
from .models import Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Blogs
        fields = '__all__'
        
class CustomUserRegister(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(widget = forms.TextInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget = forms.TextInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']