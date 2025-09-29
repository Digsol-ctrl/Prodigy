from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product-details/<slug:slug>/',views.ProductDetailView.as_view(), name='product_details'),

]