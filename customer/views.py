from django.shortcuts import render
from .models import Customer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = "login")

def list_customer(request):
    list_customer = Customer.objects.all()
    paginator = Paginator(list_customer,5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request,"customer/list-customer.html",{"page_obj": page_obj}) 
@login_required(login_url = "login")
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
    paginator = Paginator(list_customer,5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request,"customer/list-customer.html",{"page_obj": page_obj}) 
    #     list_customer = Customer.objects.all()
    #     context = {
    #         'list_customer':list_customer
    #     }

    # return render(request,"customer/list-customer.html",context) 


def update_customer(request,customer_id):

    customer = get_object_or_404(Customer, id = customer_id)
    context = {
        'customer' : customer
    }

    return render(request,"customer/update-customer.html",context) 

def update_process(request):

    if request.method == "POST":
        rq_id = request.POST.get("customer_id")
        rq_name = request.POST.get("name")
        rq_phone = request.POST.get("phone")
        rq_address = request.POST.get("address")
        Customer.objects.filter(id=rq_id).update(name = rq_name, phone = rq_phone, address = rq_address)
        list_customer = Customer.objects.all()
        context = {
            'list_customer':list_customer
        }
        return render(request,"customer/list-customer.html",context)


def delete_customer(request):
    if request.method == 'GET':
        customer_id = request.GET['customer_id']
        customer = Customer.objects.get(id = customer_id)
        customer.delete()
        context = {
            'mess' :"Xóa thành công"
        }
    return JsonResponse(context)