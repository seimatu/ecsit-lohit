from django.urls import path
from . import views

urlpatterns = [
    path('strap',views.bootstrap),
]
