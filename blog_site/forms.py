from django.forms import ModelForm
from .models import News
from django import forms

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields=['title','text','image','cat','is_published']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }