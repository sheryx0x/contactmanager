from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create_contact',views.create_contact, name='create_contact'),
    path('update_contact/<str:pk>/',views.update_contact, name='update_contact'),
    path('delete_contact/<str:pk>/',views.delete_contact, name='delete_contact'),
    
]
