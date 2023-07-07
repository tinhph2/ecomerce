from django.shortcuts import render
from .models import Course
from .forms import CourseForm
# Create your views here.

def upload_app(request):
    form_class = CourseForm
    context = {
        'form':form_class
    }
    return render(request,"upload/index.html",context) 

def process_upload(request):
    if request.method == "POST":
        rq_author = request.POST.get("inputAuthor")
        rq_inputTitle = request.POST.get("inputTitle")
        rq_inputFile = request.POST.get("inputFile")
        rq_inputDocument = request.POST.get("inputDocument")
    return render(request,"upload/index.html") 