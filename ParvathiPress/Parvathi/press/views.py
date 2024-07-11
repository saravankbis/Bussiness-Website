from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Fun 
from . import views




# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

# def Contact(request):
#     template = loader.get_template('Contact.html')
#     return HttpResponse(template.render())

    
def Contact(request):
    mydata = Contact.objects.all()
    if(mydata!=""):
        return render(request, "Contact.html",{"Contact":mydata})
    else:
        return render(request, "Contact.html")
    
def Contact(request):
    mydata = Fun.objects.all()
    return render(request, "Contact.html", {"Fun": mydata})
    
    
def Portfolio(request):
    template = loader.get_template('Portfolio.html')
    return HttpResponse(template.render())

def Sign(request):
    template = loader.get_template('Sign.html')
    return HttpResponse(template.render())

def Helpcenter(request):
    template = loader.get_template('Helpcenter.html')
    return HttpResponse(template.render())

def Products(request):
    template = loader.get_template('Products.html')
    return HttpResponse(template.render())

def addData(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        message=request.POST["message"]
        
        obj=Fun()
        obj.Name=name
        obj.Email=email
        obj.Message=message
        obj.save()
        mydata=Fun.objects.all()
        return redirect("Contact")
    return render(request,"home.html")



