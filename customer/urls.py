from django.urls import path
from .import views as v

urlpatterns = [
 path("Book",v.addcustomer,name="book"),
  path("Review",v.addreview,name="review")
]