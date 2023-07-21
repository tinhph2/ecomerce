from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def login(request):
    return render(request,"account/login.html") 

def process_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.user.is_authenticated):
                return redirect('/customer/')
        else:
            return redirect('login')

def logout(request):
    auth.logout(request)
    return render(request,"account/login.html") 

def register(request):
    return render(request,"account/register.html") 

def process_regis(request):
    if request.method == "POST":
        username = request.POST["userName"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        subject = "Welcome my shop"
        mess = f'Hi {user.username}, thanks for regis'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject, mess, email_from, recipient_list)
        return redirect('login')
    return render(request,"account/register.html") 