from django.shortcuts import render
from index.models import *

# Create your views here.
def home(request):
    all_objects = blog.objects.all()
    print all_objects

    second_object = all_objects[1]
    title_second_object = second_object.title
    context_second_object = second_object.context

    third_object = all_objects[2]
    title_third_object = third_object.title
    context_third_object = third_object.context

    template = "home.html"
    context = {
        "title2": title_second_object,
        "title3": title_third_object,
        "context2": context_second_object,
        "context3": context_third_object,
    }
    return render(request,template,context)