import django
from django.db import models
# Create your models here.


class Userx(models.Model):
    email = models.CharField(max_length=50 )
    username = models.CharField(max_length=50 )
    password = models.CharField(max_length=50)

class PaymentUser(models.Model):
    userx_id = models.ForeignKey(Userx,on_delete= models.CASCADE)
    amount = models.FloatField(default=0.0)
    payment_date= models.DateField(auto_now_add=True)
    expiration_date= models.DateField(null=True)


class Service(models.Model): 
    service_id = models.OneToOneField(PaymentUser,on_delete= models.CASCADE)
    Name = models.CharField(max_length=50 )
    description = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)

class ExpiredPayments(models.Model):
    payment_user_id= models.OneToOneField(PaymentUser,on_delete= models.CASCADE)
    penalty_fee_amount= models.FloatField(default=0.0)



