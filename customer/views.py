from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def addcustomer(request):
    if request.method=="POST":  
        name=request.POST.get("name")
        email=request.POST.get("email")
        date=request.POST.get("date")
        time=request.POST.get("time")
        id_services=request.POST.get("id_services")
        obj=customer()
        obj.name=name
        obj.email=email
        obj.date=date
        obj.time=time
        obj.id_services=id_services
        obj.save()
        return redirect("/")
    else:
        return render(request,"Book.html")

def addreview(request):
    if request.method=="POST":  
        name=request.POST.get("name")
        review=request.POST.get("review")
        obj=reviews()
        obj.name=name
        obj.review=review
        obj.save()
        return redirect("/")
    else:
        return render(request,"Review.html")