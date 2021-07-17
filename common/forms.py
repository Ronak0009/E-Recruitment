from django import forms
# from .models import AppUser
from django.utils.safestring import mark_safe
import re

class LoginForm(forms.Form):
    email = forms.CharField(label='',max_length=40,
                widget=forms.TextInput(attrs={"placeholder":"Email",
                                             "size":"40",
                                             "class":"text",
                                             "name":"email"}))
    
    password = forms.CharField(label='',max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Password",
                                             "size":"40",
                                             "class":"text",
                                             "name":"password"}))
  

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        email = str(self.cleaned_data.get("email"))
        password = str(self.cleaned_data.get("password"))

        try:
            email_not_valid = False
            if not re.search(r'^\w+$', email):
                email_error = mark_safe("Invalid email")
                email_not_valid = True
                raise forms.ValidationError(email_error)
        except forms.ValidationError as e:
            self.add_error('email', e)

        try:
            if not re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',password):
                errormsg = mark_safe('Invalid password')
                raise forms.ValidationError(errormsg)
        except forms.ValidationError as e:
            self.add_error('password', e)

        else:
            return cleaned_data

