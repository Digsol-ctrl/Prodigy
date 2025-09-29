from django.urls import path
from . import views
from django import forms
from .models import Product

app_name = 'products'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = []

