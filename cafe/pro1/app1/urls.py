from django.urls import path
from .views import *
urlpatterns =[
    path("home/",home,name="home_url"),
    path("about/",about,name="about_url"),
    path("order/",order,name="order_url"),
    path("contact/",contact,name="contact_url"),
    path("Shop/",shop,name="shop_url"),
    path("index/",index,name="index_url"),
    path("cart1/",cart,name="cart"),
    path("checkout/",checkout,name="checkout_url"),
    path("login/",Vlogin,name="login_url")
]