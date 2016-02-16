from django.shortcuts import render
from homepage.models import blog 

from .forms import BlogPosts 

# our forms class is BlogPosts
# Create your views here.
def home(request):
    all_objects= blog.objects.all()

  
    template="home.html" 
    form = BlogPosts(request.POST or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
    
    
    context={
        "formvar": form, 
       
    }
    return render(request,template,context)