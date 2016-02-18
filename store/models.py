from __future__ import unicode_literals

from django.db import models
from address.models import AddressField
from django.core.validators import RegexValidator

# Create your models here.
class Location(models.Model):
    address = AddressField()
    email = models.EmailField()
    name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    address1 = AddressField()
    address2 = AddressField(related_name='+', blank=True, null=True)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    class Meta:
        abstract = True

class Owner(Person):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Item(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    deposit = models.DecimalField(decimal_places=2, max_digits=6)
    daily_price = models.DecimalField(decimal_places=2, max_digits=6)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Picture(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

class Customer(Person):
   pass

class Booking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_dt = models.DateField()
    end_dt = models.DateField()
