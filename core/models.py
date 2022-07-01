from platform import mac_ver
from pyexpat import model
from this import d
from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key = True, verbose_name = 'CATEGORIAID')
    name = models.CharField(max_length = 25, verbose_name = 'CATEGORIANOMBRE')

    def __str__(self):
        return self.name

class Product(models.Model):
    ProductId = models.AutoField(primary_key = True, verbose_name = 'PRODUCTOID')
    name = models.CharField(max_length = 50, verbose_name = 'PRODUCTONOMBRE')
    price = models.FloatField(verbose_name = 'PRODUCTOPRECIO')
    description = models.TextField(max_length = 200, verbose_name = 'PRODUCTODESCRIPCION')
    image = models.ImageField(null =  True, blank = True, verbose_name = 'PRODUCTOIMAGEN', upload_to = 'medias')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    clientId = models.AutoField(primary_key = True, verbose_name = 'CLIENTID')
    firstName = models.CharField(max_length = 25, verbose_name = "FIRSTNAME")
    lastName = models.CharField(max_length = 30, verbose_name = "LASTNAME")
    email = models.EmailField(verbose_name = "EMAIL")
    registratedOn = models.DateTimeField()
    phoneNumber = models.CharField(max_length = 8)
    country = models.CharField(max_length = 38, verbose_name = "COUNTRY")
    state = models.CharField(max_length = 34, verbose_name = "STATE")
    city = models.CharField(max_length = 34, verbose_name = "CITY")
    place = models.CharField(max_length = 34, verbose_name = "PLACE")
    adress = models.CharField(max_length = 34, verbose_name = "ADRESS")
    
    def __str__ (self):
        return self.email

