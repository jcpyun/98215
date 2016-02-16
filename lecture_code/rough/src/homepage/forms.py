from django import forms
from django.forms import ModelForm
############################ django imports above
from .models import blog 
############################# model import above

class BlogPost(ModelForm): 
    class Meta:
        model = blog
        #fields = ['title','context']
        exclude= ['']
        