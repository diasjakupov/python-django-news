from .models import News, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields=['title','text','image','cat','is_published']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }


class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'username']