from django.shortcuts import render

# Create your views here.

def upload_app(request):
    return render(request,"upload/index.html") 