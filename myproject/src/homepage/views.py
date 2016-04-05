from django.shortcuts import render

# Create your views here.
def home(request):
    template= "home.html"
    context={
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