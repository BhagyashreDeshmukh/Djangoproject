from django.shortcuts import render,redirect
from .models import *
from owner import models as owner
# Create your views here.
def home(request):
    return render(request,"index.html")

def About(request):
    return render(request,"About.html")

def Team(request):
    return render(request,"Team.html")

def Blog(request):
    return render(request,"Blog.html")

def Book(request):
    return render(request,"Book.html")


def adddetails(request):
    if request.method=="POST":
        obj=ContactForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={'form':ContactForm}
        return render(request,"Contact.html",d)

def Serviceslist(request):
    data=owner.Service.objects.all()
    d={"obj":data}
    return render(request,"services.html",d)