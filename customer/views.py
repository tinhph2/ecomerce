from django.shortcuts import render
from .models import Customer
# Create your views here.
def list_customer(request):
    list_customer = Customer.objects.all()
    context = {
        'list_customer':list_customer
    }
    return render(request,"customer/list-customer.html",context) 

def add_customer(request):
    return render(request,"customer/add-customer.html") 

def add_new_customer(request):
    if request.method == "POST":
        rq_name = request.POST.get("name")
        rq_phone = request.POST.get("phone")
        rq_address = request.POST.get("address")
        data = Customer(name = rq_name, phone = rq_phone, address = rq_address)
        data.save()

        list_customer = Customer.objects.all()
        context = {
            'list_customer':list_customer
        }

    return render(request,"customer/list-customer.html",context) 


def update_customer(request,customer_id):
    print("customer.id"+str(customer_id))

    return render(request,"customer/update-customer.html") 