from unicodedata import category
from rest_framework import serializers
from core.models import Product, Client

class ProductSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Product 
        fields =[ 'name', 'price', 'description', 'image', 'category']

class ClientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Client
        fields =['clientId', 'firstName', 'lastName', 'email', 'registratedOn', 'phoneNumber', 'country', 'state', 'city', 'place', 'adress']