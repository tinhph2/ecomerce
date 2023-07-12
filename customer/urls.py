from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('add', views.add_customer, name="add_customer"),
    path('', views.list_customer, name='list_customer'),
    path('add_new_custom/', views.add_new_customer, name='add_new_customer'),
    path('update_customer/<int:customer_id>/',views.update_customer,name='update_customer'),
    path('update_process/', views.update_process, name='update_process'),
    path('delete_customer/', views.delete_customer, name='delete_customer'),
]