from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from accounts.decorators import allowed_users, admin_only

import datetime
import random

from .models import Employee


# Create your views here.

@login_required(login_url='login')
@admin_only
def homepage(request):
    return render(request, 'gangaa_admin/index.html')

@login_required(login_url='login')
@admin_only
def employee(request):
    return render(request, 'gangaa_admin/employee.html')

@login_required(login_url='login')
@admin_only
def create_emp(request):
    if request.method == 'POST':
        emp = Employee()
        if request.POST['password'] == request.POST['password1']:
            username = "G-" + request.POST['fname'][:1].upper() + str(format(random.randint(00000, 99999), "05")) + request.POST['lname'][:1].upper()
            try:
                user = User.objects.get(username=username)
                return render(request, 'gangaa_admin/create-new-employee.html', {'error':'This username already exists. Please retry!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=request.POST['password'])
                user.first_name = request.POST['fname']
                user.last_name = request.POST['lname']
                user.email = request.POST['email']
                group = Group.objects.get(name=request.POST['empcat'])
                user.groups.add(group)
                user.save()
                emp.employee = user
                emp.emp_type = request.POST['emptype']
                emp.contact = request.POST['contact']
                emp.address = request.POST['address']
                emp.dob = request.POST['dob']
                emp.cv = request.FILES['cv']
                emp.idproof = request.FILES['idproof']
                emp.bankpassbook = request.FILES['bankpassbook']
                emp.save()
                return render(request, 'gangaa_admin/create-new-employee.html', {'success':'The Employee account has been successfully created!'})
        else:
            return render(request, 'gangaa_admin/create-new-employee.html', {'error':'The passwords do not match.'}) 
    else:
        return render(request, 'gangaa_admin/create-new-employee.html')
