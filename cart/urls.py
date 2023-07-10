from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart_summary, name="cart-summary"),
    path('add/', views.cart_add, name="cart-add"),
    path('delete/', views.cart_delete, name="cart-add"),
    path('update', views.cart_update, name="cart-add"),
    
]