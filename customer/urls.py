from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('add', views.add_customer, name="add_customer"),
    path('list/', views.list_customer, name='list_customer'),
    
]