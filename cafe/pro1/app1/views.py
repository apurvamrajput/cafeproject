from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import login,authenticate
# from .models import Book

# Create your views here.

def index(request):
    return render(request,"index.html",{})

def home(request):
    return render(request,"home.html",{})

def about(request):
    return render(request,"about.html",{})

def contact(request):
    return render(request,"contact.html",{})

def Vlogin(request):
    form = UserForm()
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            user = authenticate(username=un,password=pwd)
            if user:
                login(request,user)
                return redirect("checkout")
    return render(request,"login.html",{"form":form})


# def book(request):
#     if request.method =="POST":
#         nm = request.POST["nm"]
#         n = request.POST.get('num')
#         e = request.POST.get('email')
#         p = request.POST.get('per')
#         d = request.POST.get('dt')
#         obj = Book(name=nm,number=n,email=e,person=p,date=d)
#         obj.save()
#         return HttpResponse("DataSave!!!!")
#
#     return render(request,"book.html",{})

def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {'products': products})

def order(request):
    return render(request,"order.html",{})

def cart(request):
    if request.user.is_authenticated:
        # print("---------")
        customer = request.user.customer
        # print(customer)
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.order_item_set.all()
        # print(items)
        # print(order)  
    else:
        items=[]
        order = {"get_cart_items":0,"get_cart_total":0}

    return render(request,"cart.html",{'items':items,"order":order})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.order_item_set.all() 
    else:
        items=[]
        order = {"get_cart_items":0,"get_cart_total":0}

    return render(request,"checkout_info.html",{'items':items,"order":order})
    




