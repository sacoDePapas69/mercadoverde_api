from django.conf.urls.static import static
from django.conf import settings
from django.urls import path 
from .views import home, product, products, form_mod_product, form_product, watch, about_us, delete

urlpatterns = [ 
    path('', home, name="home"),
    path('products/', products, name = "products"),
    path('product/<id>', product, name = " product"),
    path('update/<id>', form_mod_product, name = "update"),
    path('create/', form_product, name = "create"),
    path('watch/', watch, name = "watch"),
    path('about_us/',about_us, name = "about_us"),
    path('delete/<id>', delete, name = "delete")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)