from django.views.generic.list import ListView
from django.views.generic import DetailView,CreateView
from .models import *
from .forms import Addform
from django.shortcuts import render,redirect
# from  django.http import HttpResponse
# menu=["home","about","schoool"]
# 'menu':menu,

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'title':'home page'})

# def about(request):
#     return render(request,'about.html',{'title':'about page'})

def error_404(request,exception):
    return render(request,'404.html')

class Blogview(ListView):
    ordering='-ontime'
    model=Blog
    template_name='blog.html'

class Detail(DetailView):
    model=Blog
    template_name='article.html'

def addform(request):
    form=Addform()

    if request.method == 'POST':
        form=Addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BV')
    context={'form':form}
    return render(request,'create.html',context)


