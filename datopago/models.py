from django.db import models
#rom django.utils.translation import gettext_lazy as _
#from users.models import User
# Create your models here.



class Userx(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class PaymentUser(models.Model):
    user_id = models.OneToOneField(Userx,on_delete= models.CASCADE,primary_key=True)
    amount = models.FloatField(default=0.0)
    payment_date= models.DateField(auto_now_add=True)
    expiration_date= models.DateField(null=True)


class Service(models.Model): 
    service_id = models.OneToOneField(PaymentUser,on_delete= models.CASCADE,primary_key=True)   
    Name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)

class ExpiredPayments(models.Model):
    payment_user_id= models.OneToOneField(PaymentUser,on_delete= models.CASCADE,primary_key=True)
    penalty_fee_amount= models.FloatField(default=0.0)



