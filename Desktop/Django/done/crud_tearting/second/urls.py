from django.urls import path
from . import views

urlpatterns = [
    path('loh',views.home),
    path('about',views.about),
    path('fixed',views.fixed),
    path('call',views.call),

]