from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import ExampleFrom

# Create your views here.
def home(request):
    form = ExampleFrom()
    context = {"form":form}
    return render(request,"demo/index.html", context) 

def login(request):
    if request.method == "POST":
        form = ExampleFrom(request.POST)
        if form.is_valid():
            user = request.POST.get("user_name",'')
            password = request.POST.get("password",'')
            data = {
                "user":user,
                "password":password
            }
            return render(request,"demo/info.html", data) 
        else:
            form = ExampleFrom()
            context = {"form":form}
            return render(request,"demo/index.html",context)

def regis(request):
    return render(request,"demo/regis.html") 

