from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_countries.fields import CountryField  # type: ignore

class SingUpForm(UserCreationForm):
    country = CountryField().formfield()
    email = forms.EmailField(required=False, help_text='Email not required')
    class Meta:
        model = User
        fields =('username','email','country','password1','password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Country', 'ProfileImg']