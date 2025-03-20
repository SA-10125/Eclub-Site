from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.render_temp_blogs,name='blogs'),
    path('read/<str:pk>/',views.read_blog,name='read_blog'),
    path('new/',views.write_blog,name='new_blog'),
    path('edit/<str:pk>/',views.edit_blog,name='edit_blog'),
    path('delete/<str:pk>/',views.delete_blog,name='delete_blog'),
]
