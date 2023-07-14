from django.shortcuts import render,redirect
from django.contrib import auth
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
        
