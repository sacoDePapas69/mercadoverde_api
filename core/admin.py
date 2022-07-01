from multiprocessing.connection import Client
import site
from django.contrib import admin
from .models import Category, Product, Client

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)