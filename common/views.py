from company.models import company
from typing import ContextManager
from django.shortcuts import render
from employee.models import employee
from employee.forms import EmployeeForm
from .forms import LoginForm
import random
from company.models import company
from company.forms import CompanyForm


# Create your views here.

def main_dashboard(request,*args):
    return render(request,"common/main.html")

def registration_view(request,no,*args):
    no = no
    print(no)
    if no == 1:
        model = employee
        form = EmployeeForm
        context = {
        'form':form,
        'num':no,
        }
        return render(request,"common/reg.html",context)
    elif no == 2:
        model = company
        form = CompanyForm
        context = {
        'form':form,
        'num':no,
        }
        return render(request,"common/reg.html",context)

def login_view(request,no,*args):
    no = no
    global str_num
    if no == 1:
        form = LoginForm
        num = random.randrange(10000,99999)
        str_num = str(num)
        print(num)
        context = {
        'form':form,
        'num':num,
        'no':no,
        }
        return render(request,"common/login.html",context)
    elif no == 2:
        form = LoginForm
        num = random.randrange(10000,99999)
        str_num = str(num)
        print(num)
        context = {
        'form':form,
        'num':num,
        'no':no,
        }
        return render(request,"common/login.html",context)