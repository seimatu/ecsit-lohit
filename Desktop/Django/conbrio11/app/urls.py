from django.urls import path
from .views import Index
from . import views
from django.contrib.auth import views as auth_views

app_name='mainapp'

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('users/<int:pk>/',views.users_detail,name='users_detail'),
    path('plans/new/',views.plans_new,name='plans_new'),
    path('plan/<str:category>/',views.plans_category,name='plans_category'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
