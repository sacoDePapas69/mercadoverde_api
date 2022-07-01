from django.urls import path 
from .views import product_list, client_list

urlpatterns=[ 
    path('products', product_list, name = "product_list"),
    path('clients', client_list, name = "client_list"),
]