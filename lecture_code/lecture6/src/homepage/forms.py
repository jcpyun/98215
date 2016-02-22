from django import forms 
from django.forms import ModelForm

from .models import blog 

class BlogPosts(ModelForm):
    class Meta:
        model = blog
        #fields= ['title','context','after','initial']
        exclude= ['']