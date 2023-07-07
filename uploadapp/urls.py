from django.contrib import admin
from django.urls import path
from uploadapp import views

urlpatterns = [
    path('', views.upload_app, name="upload_app"),
    path('upload/', views.process_upload, name='process_upload')
]