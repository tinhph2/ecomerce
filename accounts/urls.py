from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('process_login', views.process_login, name="process_login"),
]