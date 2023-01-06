from django.urls import path
from .import views as v

urlpatterns = [
    path("",v.home,name="home"),
    path("About",v.About,name="about"),
    path("Team",v.Team,name="team"),
    path("Blog",v.Blog,name="blog"),
    path("Book",v.Book,name="book"),
    path("Order",v.adddetails,name="order"),
    path("Services",v.Serviceslist,name="services"),
]