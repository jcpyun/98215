from django.shortcuts import render

from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home(request):
    template="home.html" 
    WOW = blog.objects.all()[0]
    wowafter= WOW.after
    print wowafter
    context={
        "thisisavar": wowafter
    }
    return render(request,template,context)