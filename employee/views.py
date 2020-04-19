from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from accounts.decorators import allowed_users, admin_only

import datetime
import random

from .models import Shop
from gangaa_admin.models import Employee


# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['marketing'])
def marketing(request):
    return render(request, 'employee/marketing.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['marketing'])
def create_shop(request):
    if request.method == 'POST':
        shop = Shop()
        username = "G-" + str(format(random.randint(00000, 99999), "05"))
        shop.shop_id = username
        try:
            user = User.objects.get(username=username)
            return render(request, 'employee/create-shop.html', {'error':'This Shop already exists!'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username)
            user.first_name = request.POST['merchantfname']
            user.last_name = request.POST['merchantlname']
            user.email = request.POST['email']
            group = Group.objects.get(name='merchant')
            user.groups.add(group)
            user.is_active = False
            user.save()
            shop.merchant = user
            shop.shop_name = request.POST['shopname']
            shop.shop_type = request.POST['shoptype']
            shop.contact = request.POST['contact']
            shop.address = request.POST['address']
            shop.doe = request.POST['doe']
            shop.gst = request.POST['gst']
            shop.gstcert = request.FILES['gstcert']
            shop.idproof = request.FILES['idproof']
            shop.location_lat = request.POST['lat']
            shop.location_lon = request.POST['long']
            shop.save()
            return render(request, 'employee/create-shop.html', {'success':'The Shop has been successfully created!'})
    else:
        return render(request, 'employee/create-shop.html')
