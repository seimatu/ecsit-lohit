from django.urls import path
from . import views
from .views import Home,ProductDetail
from cart.views import add_to_cart,remove_from_cart,CartView,decreaseCart

from django.contrib.auth import views as auth_views


app_name='mainapp'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('cart/',CartView,name='cart-home'),
    path('cart/<slug>',add_to_cart,name='cart'),
    # path('product/<slug>',views.Detail,name='detail'),
    path('detail/<slug>',ProductDetail.as_view(),name='detail'),
    path('remove/<slug>',remove_from_cart,name='remove-cart'),
    path('decrease-cart/<slug>',decreaseCart,name='decrease-cart'),

]
