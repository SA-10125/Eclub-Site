from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.render_simple_homepage,name='home'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
]
