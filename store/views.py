from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404
# Create your views here.
# def home(request):
#     return render(request,"store/index.html") 

def home(request):
    all_product = Product.objects.all()
    context = {"my_product":all_product}
    return render(request,"store/index.html", context) 

def product_info(request, product_slug):
    product = get_object_or_404(Product,slug =  product_slug)
    context = {"product": product}
    return render(request,"store/product-info.html", context) 