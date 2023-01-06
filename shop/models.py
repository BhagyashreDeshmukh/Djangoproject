from django.db import models

# Create your models here.
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    class Meta:
        db_table="Contact"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields="__all__"
