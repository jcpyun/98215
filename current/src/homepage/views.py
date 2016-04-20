from django.shortcuts import render
from homepage.models import blog 

from .forms import BlogPosts 


from django.contrib.auth import authenticate,login,logout
from wow import settings
from django.contrib.auth.models import User #this is for auth model
# Create your views here.
def home(request):
    template= "home.html"
    context={
    }
    return render(request,template,context) 
def aboutme(request):
    template= "aboutme.html"
    context={
    }
    return render(request,template,context) 
def contact(request):
    template= "contact.html"
    form = BlogPosts(request.POST or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save()
    context={
        "formvar": form,
    }
    return render(request,template,context) 
def positions(request):
    template= "positions.html"
    context={
    }
    return render(request,template,context) 
def media(request):
    template= "media.html"
    context={
    }
    return render(request,template,context) 