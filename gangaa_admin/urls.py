from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('employees/', views.employee, name="employee"),
    path('employees/create-new-employee', views.create_emp, name="create_emp"),
]