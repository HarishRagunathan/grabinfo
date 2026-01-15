from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post
from django import forms

class signupform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'user','placeholder':'Enter your username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'email','placeholder':'Enter your E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'password','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'password','placeholder':'Re-Enter your password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'content','post_image']  

    