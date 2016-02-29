from django import forms
from django.forms import ModelForm

from .models import blog

class BlogPost(ModelForm):
	class Meta:
		model = blog
		exclude = ['']