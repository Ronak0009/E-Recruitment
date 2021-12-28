from company.models import company
from typing import ContextManager
from django.shortcuts import render,redirect
from employee.models import candidate
from employee.forms import candidateForm
from .forms import LoginForm
from company.models import company
from company.forms import CompanyForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django_email_verification import send_email
from .methods import id_generator
import random

def redirect_to_dashboard(request, *args):
    return redirect('/main-dashboard')
    
def main_dashboard(request,*args):
    return render(request,"common/main.html")

def login_process_view(request,no,*args):
    if not request.user.is_anonymous:
        userEmail = request.user.email
        user = User.objects.filter(email=userEmail, is_active=1)
        if user:
            if user[0].groups.filter(name = 'company'):
                return redirect('/company/profile')
            elif user[0].groups.filter(name = 'candidate'):
                return redirect('/candidate/profile/')
        # user = company.objects.filter

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        context = {
        'form':form,
        'no':no,
        }
        print(no)
        if form.is_valid():
            details = form.cleaned_data
            username_input = details['email']
            passwd_input = details['password']
            user_valid = User.objects.filter(username=username_input)
            if user_valid.count() == 0:
                raise ValidationError("The user does not exist")
            else:
                user = user_valid[0]
                groups = user.groups.all()
                if not user.is_active:
                    if no == 1:
                        try:
                            if groups.filter(name = 'candidate'):
                                return redirect('/not-verified')
                            else:
                                raise ValidationError("Incorrect username or password")
                        except ValidationError as e:
                            form.add_error('password',e)
                            return render(request, 'common/login.html', context)
                    elif no == 2:
                        try:
                            if groups.filter(name = 'company'):
                                login(request,user)
                                return redirect('/not-verified')
                            else:
                                raise ValidationError("Incorrect username or password")
                        except ValidationError as e:
                            form.add_error('password',e)
                            return render(request, 'common/login.html', context)
            try:
                user = authenticate(request,username=username_input,
                            password=passwd_input)
                if user is None:
                    raise ValidationError("Incorrect username or password")
            except ValidationError as e:
                form.add_error('password',e)
                return render(request, 'common/login.html', context)
            
            if user is not None:
                
                groups = user.groups.all()
                if no == 1:
                    try:
                        if groups.filter(name = 'candidate'):
                            login(request,user)
                            return redirect('/candidate/profile')
                        else:
                            raise ValidationError("Incorrect username or password")
                    except ValidationError as e:
                        form.add_error('password',e)
                        return render(request, 'common/login.html', context)
                elif no == 2:
                    try:
                        if groups.filter(name = 'company'):
                            login(request,user)
                            return redirect('/company/profile')
                        else:
                            raise ValidationError("Incorrect username or password")
                    except ValidationError as e:
                        form.add_error('password',e)
                        return render(request, 'common/login.html', context)

        else:
            return render(request, 'common/login.html', context)
    else:
        
        form = LoginForm()
        context = {
        'form':form,
        'no':no
        }
        return render(request, 'common/login.html', context)

    return render(request,"common/login.html")

def not_verified(request,*args):
    return render(request,"common/not-verified.html")

def registration_view(request,no,*args):
    no = no
    if no == 1:
        model = candidate
        form = candidateForm
        context = {
        'form':form,
        'num':no,
        }
        return render(request,"common/reg.html",context)
    elif no == 2:
        model = company()
        form = CompanyForm()
        context = {
        'form':form,
        'num':no,
        }
        return render(request,"common/reg.html",context)

def company_registration(request,*args):
    no=2
    # companyForm = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            details = form.cleaned_data
            new_company_name = details['company_name']
            new_passwd = details['password']
            new_email = details['email']
            new_mobile = details['mobile']
            new_account_id = id_generator()
            
            try:
                validate_password(new_passwd, form)
            except ValidationError as e:
                form.add_error('password', e)
                return render(request, "common/reg.html", {'form': form})


            newCompany = company(
                        company_name=str(new_company_name),
                        password=str(new_passwd),
                        account_id=str(new_account_id),
                        mobile=str(new_mobile),
                        email=str(new_email.lower()),
                        )

            newUser = User.objects.create_user(
                        username=str(new_email.lower()),
                        password=str(new_passwd),
                        email=str(new_email.lower()),
            )
            
            newUser.is_active = False
            company_group = Group.objects.get(name='company') 
            company_group.user_set.add(newUser)
            # newUser.set_password(str(new_passwd))
            # newUser.save()
            send_email(newUser)
            newCompany.save()
            return redirect("../pending-account")
    else:
        form = CompanyForm(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'

    context ={
        'form':form,
        'num':no,
    }
    return render(request,"common/reg.html",context)


def candidate_registration(request,*args):
    no=1
    candidateform = candidateForm
    if request.method == "POST":
        print('in post')
        form = candidateform(request.POST or None)
        if form.is_valid():
            print('isvalid')
            details = form.cleaned_data
            new_name = details['firstName']
            new_lname = details['lastName']
            new_passwd = details['password']
            new_email = details['email']
            new_mobile = details['mobile']
            new_university = details['university']
            new_account_id = id_generator()
            
            try:
                validate_password(new_passwd, form)
            except ValidationError as e:
                form.add_error('password', e)
                return render(request, "common/reg.html", {'form': form})


            newCandidate = candidate(
                        firstName=str(new_name),
                        lastName=str(new_lname),
                        password=str(new_passwd),
                        account_id=str(new_account_id),
                        mobile=str(new_mobile),
                        email=str(new_email.lower()),
                        university = str(new_university)

                        # isActive=False
                        )

            # newUser = User.objects.create_user(
            #             username=str(new_username),
            #             password=str(new_passwd),
            #             first_name=str(new_fName.capitalize()),
            #             last_name=str(new_lName.capitalize()),
            #             email=str(new_email.lower()),
            # )

            # newUser.save()
            
            newUser = User.objects.create_user(
                        first_name=str(new_name),
                        last_name=str(new_lname),
                        username=str(new_email.lower()),
                        password=str(new_passwd),
                        email=str(new_email.lower()),
            )
            
            # newUser.groups.set([candidate_group])
            newUser.is_active = False
            candidate_group = Group.objects.get(name='candidate') 
            candidate_group.user_set.add(newUser)
            # newUser.save()
            send_email(newUser)
            newCandidate.save()
            return redirect("../pending-account")
    else:
        form = candidateForm(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'
    context ={
        'form':form,
        'num':no,
    }

    return render(request,"common/reg.html",context)

def pending_view(request,*args):
    return render(request,"common/pending_account.html")

def login_view(request,no,*args):
    if not request.user.is_anonymous:
        userEmail = request.user.email
        user = User.objects.filter(email=userEmail, is_active=1)
        if user:
            if user[0].groups.filter(name = 'company'):
                return redirect('/company/profile')
            elif user[0].groups.filter(name = 'candidate'):
                return redirect('/candidate/profile')
                
    no = no
    form = LoginForm()
    context = {
        'form':form,
        'no':no,
        }
    return render(request,"common/login.html",context)


def video_chat(request,*args):
    return render(request,"common/vchat.html")

def logout_view(request,*args):
    logout(request)
    return redirect('/main-dashboard/')

# def sendEmail(request,*args):
#     password = request.POST.get('password')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     user = get_user_model().objects.create(username = username, password=password)