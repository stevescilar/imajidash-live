from enum import unique
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models
import os
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .utils import receipt_no , shipping_mark

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SalesAgent(models.Model):
    name = models.CharField(max_length=50)
    contact = PhoneNumberField(blank=True,null=True,unique=True)
    
    def __str__(self):
        return self.name
# Create your models here....git

class Client(models.Model):
    name = models.CharField(max_length=200)
    # email = models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    contact = PhoneNumberField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sales_agent = models.ForeignKey(SalesAgent,on_delete = models.SET_NULL,null=True)
    
    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return f'{self.name} - {self.sales_agent} (Sales Person)'

class ImajiAgent(models.Model):
    name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    #contact to be addedd.
    

    def __str__(self):
        return "%s" % (self.name)
#create a remarks/comments center 

# ------------------------------------------China Warehouse Logic---------------------------------------------#
#-------------------------------------------separation of matters --------------------------------------#
# -------*****------------------------------Receiving ----------------------------------------------------#
class ReceivedCargoChina(models.Model):
    client_name = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    goods = models.CharField(max_length=200,null=True)
    cbm = models.IntegerField(null=True)
    ctns = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    sales_agent = models.ForeignKey(SalesAgent,on_delete = models.SET_NULL,null=True)
    remark = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    # ADD RECEIVING AGENT LATER

    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s - %s" % (self.client_name,self.goods)


# yiwu warehouse
class ReceivedCargoYiwu(models.Model):
    client_name = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    goods = models.CharField(max_length=200,null=True)
    cbm = models.IntegerField(null=True)
    ctns = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    sales_agent = models.ForeignKey(SalesAgent,on_delete = models.SET_NULL,null=True)
    remark = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    # ADD RECEIVING AGENT LATER.

    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s - %s" % (self.client_name,self.goods)
# bulk from china
class DispatchCargoYiwu(models.Model):
    client_name = models.ForeignKey(Client,related_name='dispatchyiwu_name', on_delete=models.SET_NULL,null=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    receipt_no = models.CharField(
           max_length = 6,null=True,
           blank=True,
           editable=False,
           unique=True,
           default=receipt_no)
    goods = models.OneToOneField(ReceivedCargoYiwu,on_delete=models.SET_NULL,null=True,unique=True)#to be tried in productin
    cbm = models.CharField(max_length=200,null=True)
    ctns = models.CharField(max_length=200,null=True)
    weight = models.CharField(max_length=200,null=True)
    shipping_mark= models.CharField(
           max_length = 6, null=True,
           blank=True,
           editable=False,
           unique=True,
           default=shipping_mark)
    container_number = models.CharField(max_length=50,verbose_name='Cont-N0:')
    remark = models.TextField(null=True,verbose_name='Remarks')  
    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s" % (self.goods)
class  MsgFromChina(models.Model):
    client_name = models.ForeignKey(ReceivedCargoChina,related_name='client_rchina', on_delete=models.SET_NULL,null=True)
    goods = models.ForeignKey(ReceivedCargoChina,on_delete=models.SET_NULL,null=True)
    status = models.ForeignKey(ReceivedCargoChina,related_name='cargo_is_active',on_delete=models.CASCADE,null=True)
    send = models.BooleanField(default=False)
    def __str__(self):
       return "%s" % (self.goods)

    def save(self, *args, **kwargs):
        if self.send == True:
            account_sid = 'AC407d27253901e5e7818431ca6e4782a8'
            auth_token = '9b2322bdadf47c7a087e06c36dfea58e'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                        body="Your Cargo was received in China warehouse",
                        from_='+15152202770',
                        to='+254705549257'
                    )

            print(message.sid)
        return super().save(*args, **kwargs)


# -------*****------------------------------Dispatching ----------------------------------------------------#
class DispatchCargoChina(models.Model):
    client_name = models.ForeignKey(Client,related_name='dispatchchina_name', on_delete=models.SET_NULL,null=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    receipt_no = models.CharField(
           max_length = 6,null=True,
           blank=True,
           editable=False,
           unique=True,
           default=receipt_no)
    goods = models.OneToOneField(ReceivedCargoChina,on_delete=models.SET_NULL,null=True,unique=True)#to be tried in productin
    cbm = models.CharField(max_length=200,null=True)
    ctns = models.CharField(max_length=200,null=True)
    weight = models.CharField(max_length=200,null=True)
    shipping_mark= models.CharField(
           max_length = 6, null=True,
           blank=True,
           editable=False,
           unique=True,
           default=shipping_mark)
    container_number = models.CharField(max_length=50,verbose_name='Cont-N0:')
    remark = models.TextField(null=True,verbose_name='Remarks')  
    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s" % (self.goods)

# Yiwu-dispatch

# -------*****------------------------------End of China OPS ----------------------------------------------------#

# ------------------------------------------kENYA Warehouse Logic---------------------------------------------#
#-------------------------------------------separation of concerns --------------------------------------#
# -------*****------------------------------Receiving ----------------------------------------------------#

class ReceivedCargoKenya(models.Model):
    client_name = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    goods = models.OneToOneField(DispatchCargoChina,on_delete=models.SET_NULL,null=True,unique=True)
    cbm = models.CharField(max_length=200,null=True)
    ctns = models.CharField(max_length=200,null=True)
    weight = models.CharField(max_length=200)
    remark = models.TextField(null=True)
    # ADD RECEIVING AGENT LATER

    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s" % (self.client_name)

# ---------------------------------------------------Dispatching Kenya ----------------------------------------------------#
class DispatchCargoKenya(models.Model):
    client_name = models.ForeignKey(Client,related_name='dispatch_name', on_delete=models.SET_NULL,null=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_number = models.CharField(max_length=50)
    goods = models.OneToOneField(ReceivedCargoKenya,on_delete=models.SET_NULL,null=True,unique=True)#to be tried in productin
    cbm = models.CharField(max_length=200,null=True)
    ctns = models.CharField(max_length=200,null=True)
    weight = models.CharField(max_length=200,null=True)
    received_by = models.CharField(max_length=50,null=True)
    Receiver_contact = PhoneNumberField()
    remark = models.TextField(null=True,verbose_name='Remarks')
   
    
    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s - %s" % (self.goods, self.Receiver_contact)

# ---------------------------------------------- end of line ----------------------------------------------#
#------------------------------------------End of kenya OPS ---------------------------------------------#



class Remark(models.Model):
    host = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
    subject = models.CharField(max_length=200,null=True)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True,blank=True)
    participant = models.ManyToManyField(User, related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.subject #not clear about it


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remark = models.ForeignKey(Remark, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body