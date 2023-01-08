from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import login,logout,authenticate
from customer import models as customer
from shop import models as shop
from owner import models as owner
from django.db.models import Q
# Create your views here.
def adduser(request):
    if request.method=="POST":
        obj=UserCreationForm(request.POST)
        obj.save()
        return redirect("/Owner-Login")
    else:
        d={"form":UserCreationForm}
        return render(request,"Register.html",d)

def checkuser(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/Owner-Admin")
        else:
            return redirect("/Owner-Login")
    else:
        d={"form":LoginForm}
        return render(request,"form.html",d)

def lgot(request):
    logout(request)
    return redirect("/")

def reviewlist(request):
    data=customer.reviews.objects.all()
    d={"obj":data}
    return render(request,"Viewreview.html",d)

def Customerlist(request):
    data=customer.customer.objects.all()
    d={"obj":data}
    return render(request,"Myorders.html",d)

def inquiry(request):
    data=shop.Contact.objects.all()
    d={"obj":data}
    return render(request,"Inquiry.html",d)

def addservice(request):
    if request.method=="POST":
        obj=AddServiceForm(request.POST)
        obj.save()
        return redirect("/Owner-Admin")
    else:
        d={"form":AddServiceForm}
        return render(request,"Addservices.html",d)

def Admin(request):
    total_appoinment = customer.customer.objects.all().count()
    total_review = customer.reviews.objects.all().count()
    total_Inquiry = shop.Contact.objects.all().count()

    context = {
        'total_appoinment': total_appoinment,
        'total_review': total_review,
        'total_Inquiry': total_Inquiry
    }
    return render(request, 'Admin.html', context)

def ourservice(request):
    data=owner.Service.objects.all()
    d={"obj":data}
    return render(request,"ourservices.html",d)

def delete(request,id):
    obj=owner.Service.objects.get(id=id)
    obj.delete()
    return redirect("/Owner-ourservices")

def edit(request,id):
    obj=owner.Service.objects.get(id=id)
    if request.method=="POST":
        Service=AddServiceForm(request.POST,instance=obj)
        Service.save()
        return redirect("/Owner-ourservices")
    else:
        Service=AddServiceForm(instance=obj)
        d={"form":Service}
        return render(request,"Edit.html",d)

def deletereview(request,id):
    obj=customer.reviews.objects.get(id=id)
    obj.delete()
    return redirect("/Owner-viewreview")

def Order_search(request):
    form=customer.customer.objects.all()
    if request.method=="GET":
        srch=request.GET.get("srch")
        print(srch)
        if srch!=None:
            form=customer.customer.objects.filter(id_services__icontains=srch)
            print(form)
    return render(request,"Myorders.html",{"form":form})

def deleteinquiry(request,id):
    obj=shop.Contact.objects.get(id=id)
    obj.delete()
    return redirect("/Owner-inquiry")
