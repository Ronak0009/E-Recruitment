from company.models import company
from django import forms
from django.db import models
from employee.models import employee
import re
import pandas as pd
from django.utils.safestring import mark_safe


class CompanyForm(forms.ModelForm):
    email = forms.EmailField(label="",
                widget=forms.EmailInput(attrs={"placeholder":"Email",
                                             "size":"40",
                                             'type':"email",
                                             "class":"text"}))
    mobile=forms.CharField(label="",min_length=10, max_length=10,
                widget=forms.TextInput(attrs={"placeholder":"Mobile",
                                             "size":"40",
                                             "class":"text"}))
    company_name = forms.EmailField(label="",
                widget=forms.EmailInput(attrs={"placeholder":"Company Name",
                                             "size":"40",
                                             "class":"text"}))
    reg_no = forms.EmailField(label="",max_length=25,
                widget=forms.EmailInput(attrs={"placeholder":"Registration Number",
                                             "size":"40",
                                             "class":"text"}))

    password = forms.CharField(label="",min_length=8, max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Password",
                                             "size":"40",
                                             "class":"text"}))
    confirm_password = forms.CharField(label="",min_length=8, max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Re-Password",
                                             "size":"40",
                                             "class":"text"}))

    class Meta:
        model = company
        fields = [
            'email',
            'mobile',
            'company_name',
            'reg_no',
            'password',
            'confirm_password',
        ]

    def clean(self,*args,**kwargs):
        cleaned_data = super.clean()
        email = str(self.cleaned_data.get("email"))
        mobile = str(self.cleaned_data.get("mobile"))
        reg_no = str(self.cleaned_data.get("reg_no"))
        password = str(self.cleaned_data.get("passwd"))
        confirm_password = str(self.cleaned_data.get("confirm_passwd"))

     # validates password strength
        try:
            if not re.search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',password):
                errormsg = mark_safe('Password must contain at least</br>1 upper case letter,</br>1 lower case letter,</br>1 digit and 1 special symbol.')
                raise forms.ValidationError(errormsg)
        except forms.ValidationError as e:
            self.add_error('password', e)

        # checks if password and confirm password are same
        try:
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
        except forms.ValidationError as e:
            self.add_error('confirm_password', e)

        
         # validates mobile number
        try:
            mobile_not_valid = False
            if not re.search("^[0-9]{10}$",mobile):
                mobile_error = "Not a valid phone number"
                mobile_not_valid = True
                raise forms.ValidationError("Not a valid phone number")
        except forms.ValidationError as e:
            self.add_error('mobile', e)
        
        # if mobile is valid, checks if mobile is already used
        if mobile_not_valid == False:
            try:
                if employee.objects.filter(mobile=mobile).exists():
                    mobile_exists_error = 'This mobile number is already</br>associated with an account.'
                    mobile_exists_error = mark_safe(mobile_exists_error)
                    raise forms.ValidationError(mobile_exists_error)
            except forms.ValidationError as e:
                self.add_error('mobile', e)

          # validates email
        try:
            email_not_valid = False
            if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
                email_error = "Not a valid email"
                email_not_valid = True
                raise forms.ValidationError(email_error)
        except forms.ValidationError as e:
            self.add_error('email', e)
        
        # if email is valid, checks if email is already used

        if email_not_valid == False:
            try:
                if employee.objects.filter(email=email).exists():
                    email_exists_error = 'This email is already associated</br>with an account'
                    email_exists_error = mark_safe(email_exists_error)
                    raise forms.ValidationError(email_exists_error)
            except forms.ValidationError as e:
                self.add_error('email', e)
            else:
                return cleaned_data
        else:
            return cleaned_data


        #validate registration number

        # if reg_no_not_valid == False:
        try:
            if company.objects.filter(reg_no=reg_no).exists():
                reg_no_exists_error = 'This registration number is already</br>associated with an account.'
                reg_no_exists_error = mark_safe(reg_no_exists_error)
                raise forms.ValidationError(reg_no_exists_error)
        except forms.ValidationError as e:
            self.add_error('reg_no', e)