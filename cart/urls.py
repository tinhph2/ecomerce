from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_add"),
    path('update', views.cart_update, name="cart_add"),
    
]