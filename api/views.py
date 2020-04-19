from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth

from rest_framework import viewsets, permissions
from .models import Store
from .serializers import StoreSerializer

# Create your views here.

class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer