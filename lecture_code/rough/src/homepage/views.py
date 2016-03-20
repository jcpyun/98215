from django.shortcuts import render
from homepage.models import blog 

from .forms import BlogPosts 

# our forms class is BlogPosts
# Create your views here.

##############     Authentication       ###############
from django.contrib.auth import authenticate,login,logout
from helloworld import settings
from django.contrib.auth.models import User #this is for auth model
######################################################
def home(request):
    all_objects= blog.objects.all()
    zero_object= all_objects[0]
    zero_objects_context=zero_object.context
  
    template="home.html" 
    form = BlogPosts(request.POST or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
    
    
    context={
        "formvar": form,
        "all_objects":all_objects, 
        "zero_object":zero_object,
        "zero_objects_context":zero_objects_context,
        
    }
    return render(request,template,context)