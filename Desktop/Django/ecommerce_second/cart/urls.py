from django.urls import path
from . import views
from .views import Home,ProductDetail,check
from cart.views import add_to_cart,remove_from_cart,CartView,decreaseCart
from django.contrib.auth import views as auth_views


app_name='subapp'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('checkout/',check.as_view(),name='checkout'),

]
