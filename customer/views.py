from django.shortcuts import render

# Create your views here.
def list_customer(request):
    return render(request,"customer/list-customer.html") 

def add_customer(request):
    return render(request,"customer/add-customer.html") 