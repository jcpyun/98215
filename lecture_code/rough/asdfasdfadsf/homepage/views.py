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
import json
import urllib
import time
import math
import re
import os

module_dir = os.path.dirname(__file__)  # get current directory
symbolslist = os.path.join(module_dir, 'allsymbols.txt')


symbolslist= symbolslist.split("\n")

def generateSymbolDaily():
    counter=0

    for symbol in symbolslist:
        # myfile= open("dailyPrices/"+symbol+ ".txt","w+")
        # myfile.close()
        htmltext= urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
        try:
            data = json.load(htmltext)
            datapoints= data["data_values"]
        except ValueError:
            continue
#           myfile = open("dailyPrices/"+symbol + ".txt", "a")

        for point in datapoints:
            print point,datapoints
                #myfile.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
        #    myfile.close()
        counter +=1

        print "processed quotes:", counter
generateSymbolDaily()



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