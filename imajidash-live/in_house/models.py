from django.db import models
from dashboard.models import Client,SalesAgent
# Create your models here
class offloadedCargo(models.Model):

    CONT_ORIGIN = (
        ('Yiwu','Yiwu'),
        ('Quanzhou','Quanzhou'),
    )

    container_origin = models.CharField(max_length=10,choices=CONT_ORIGIN, default='Quanzhou')
    container_number = models.CharField(max_length=10,null=True)
    client_name = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    goods = models.CharField(max_length=200,null=True)
    cbm = models.FloatField(null=True,blank=True)
    ctns = models.IntegerField(null=True)
    weight = models.FloatField(null=True,blank=True)
    total_amount = models.FloatField(null=True,blank=True)
    paid_amount = models.FloatField(null=True,blank=True)
    sales_agent = models.ForeignKey(SalesAgent,on_delete = models.SET_NULL,null=True)
    remarks = models.TextField(null=True)
    is_cleared = models.BooleanField(default=False)

    # ADD RECEIVING AGENT LATER.
    class meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return "%s" % (self.client_name)

