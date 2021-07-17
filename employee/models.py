from django.db import models

# Create your models here.

class employee(models.Model):
    account_id = models.CharField(max_length=20,
                verbose_name="Account Id",default='',primary_key=True)

    email = models.EmailField(max_length=70,
                    verbose_name="Email")
    
    mobile = models.CharField(max_length=10,
               verbose_name="Mobile Number")
    
    password = models.CharField(max_length=70,
                    verbose_name="Password")