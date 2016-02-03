from django.shortcuts import render

from homepage.models import blog 
# Create your views here.
def home(request):
    all_objects= blog.objects.all()
    first_object= all_objects[0]
    title_first_object= first_object.title 
    template="home.html" 
    context={
        "variable1": all_objects,
        "variable2": first_object, 
        "WOWTHISISAVARIABLE": title_first_object,
    }
    return render(request,template,context)