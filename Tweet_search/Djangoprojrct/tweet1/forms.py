from django import forms
from .models import Tweet1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Tweet1Form(forms.ModelForm):
    class Meta:
        model = Tweet1
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
       model = User
       fields = ('username','email', 'password1', 'password2')    

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Tweets', max_length=100)
    