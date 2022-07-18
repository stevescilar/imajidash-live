from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=300)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.name}"