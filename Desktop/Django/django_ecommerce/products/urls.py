from django.urls import path
from . views import Home
from cart.views import add_to_cart,remove_from_cart,CartView,decreaseCart

from django.contrib.auth import views as auth_views

app_name='mainapp'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    # path('product/<slug>/', ProductDetail.as_view(),name='product'),
    path('cart/',CartView,name='cart-home'),
    path('cart/<slug>',add_to_cart,name='cart'),
    path('remove/<slug>',remove_from_cart,name='remove-cart'),
    path('decrease-cart/<slug>',decreaseCart,name='decrease-cart'),

]
