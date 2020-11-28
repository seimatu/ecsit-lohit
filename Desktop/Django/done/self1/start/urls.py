from django.urls import path

from . import views


urlpatterns = [
path('free',views.free),
path('ad',views.home),
path('create',views.create_info,
name='create_info')
]
