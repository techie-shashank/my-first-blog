from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','email','password']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','password']	

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio','location','birth_date','photo']