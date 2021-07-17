from django.db import models

# Create your models here.


class company(models.Model):
    account_id = models.CharField(max_length=20,
                verbose_name="Account Id",default='',primary_key=True)
    
    company_name = models.CharField(max_length=100,
                verbose_name="Company Name")
    
    reg_no = models.CharField(max_length=25,
                verbose_name="Registration Number",unique=True)

    email = models.EmailField(max_length=70,
                    verbose_name="Email")
    
    mobile = models.CharField(max_length=10,
               verbose_name="Mobile Number")
    
    password = models.CharField(max_length=70,
                    verbose_name="Password")
