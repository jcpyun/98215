from django.shortcuts import render
from .models import * 

from .forms import BlogPost 
# Create your views here.
def home(request):
    all_object = blog.objects.all() 
    zero_object= all_object[0]
    first_object= all_object[1]
    zero_object_title= zero_object.title 
    form = BlogPost(request.POST or None) #### This is our Form 
    ######## underneeth is save code
    if form.is_valid():
        poop = form.save(commit = 'false')
        poop.save()
    ####### above is save code
    
    template="home.html" 
    context={
    "form" : form, 
    "all_object" : all_object, 
    "zero_object" : zero_object,
    "first_object" : first_object, 
    "zero_object_title" : zero_object_title, 
    }
    return render(request,template,context)