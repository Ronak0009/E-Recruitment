from django.shortcuts import render

# Create your views here.

def home_view(request,*args):
    return render(request,"employee/home.html")

def interest_view(request,*args):
    return render(request,"employee/interest.html")

def recruitment_view(request,*args):
    return render(request,"employee/recruitment.html")

def profile_view(request,*args):
    return render(request,"employee/profile.html")
