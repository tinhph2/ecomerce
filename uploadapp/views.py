from django.shortcuts import render

# Create your views here.

def upload_app(request):
    return render(request,"upload/index.html") 

def process_upload(request):
    if request.method == "POST":
        rq_author = request.POST.get("inputAuthor")
        rq_inputTitle = request.POST.get("inputTitle")
        
    return render(request,"upload/index.html") 