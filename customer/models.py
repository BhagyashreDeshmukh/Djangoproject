from django.db import models
from django import forms
from django.contrib.auth.models import User
class customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    id_services=models.CharField(max_length=50)
    class Meta:
        db_table="customer"

class customerForm(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"

class reviews(models.Model):
    name=models.CharField(max_length=20)
    review=models.CharField(max_length=50)
    class Meta:
        db_table="reviews"

class reviewForm(forms.ModelForm):
    class Meta:
        model=reviews
        fields="__all__"

