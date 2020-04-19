from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from accounts.decorators import allowed_users, admin_only

import datetime
import random

@login_required(login_url='login')
@admin_only
def stores(request):
    return render(request, 'store/all_stores.html')