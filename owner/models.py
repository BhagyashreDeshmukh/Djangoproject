from django.db import models

# Create your models here.
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)

class Service(models.Model):
    ServiceName = models.CharField(max_length=25)
    Cost = models.IntegerField()

    class Meta:
        db_table="Services"

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields="__all__"
