from django.urls import path
from .import views as v

urlpatterns = [
        path("Login",v.checkuser,name="log"),
        path("Register",v.adduser,name="reg"),
        path("Logout",v.lgot,name="logout"),
        path("Admin",v.Admin,name="admin"),
        path("Myorders",v.Customerlist,name="Myorders"),
        path("viewreview",v.reviewlist,name="viewreview"),
        path("inquiry",v.inquiry,name="inquiry"),
        path("services",v.addservice,name="services"),
        path("ourservices",v.ourservice,name="ourservices"),
        path("delete/<int:id>",v.delete,name="delete"),
        path("edit/<int:id>",v.edit,name="edit"),
        path("deletereview/<int:id>",v.deletereview,name="deletereview"),
        path("deleteinquiry/<int:id>",v.deleteinquiry,name="deleteinquiry"),
        path("OrderSearch",v.Order_search,name="search")
]
