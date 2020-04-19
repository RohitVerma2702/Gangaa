from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('marketing/', views.marketing, name="marketing"),
    path('marketing/shop/create-new-shop', views.create_shop, name="create_shop"),
]