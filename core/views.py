from django.shortcuts import render, redirect
from core.models import Product, Category
from .forms import ProductForm

# Create your views here.

def home(request):
    categorias = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {"categorias":categorias, "products": products})

def product(request, id):
    product = Product.objects.get(ProductId = id)
    return render(request, 'product.html', product)

def products(request):
    categorias = Category.objects.all()
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context,  {"categorias":categorias, "products": products})

def about_us(request):
    categorias = Category.objects.all()
    return render(request, 'about_us.html',  {"categorias":categorias, "products": products})

#THIS IS THE ADMINISTRATION SECTION

def form_product(request):
    categorias = Category.objects.all()
    #vehiculo_form=VehiculoForm()
    if request.method=='POST': 
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('watch')
    else:
        product_form= ProductForm()
    return render(request, 'c_product.html', {'product_form': product_form})

def watch(request):
    categorias = Category.objects.all()
    products = Product.objects.all()
    products = {
        'products': products
    }
    return  render(request, 'watch.html', products)

def form_mod_product(request,id):
    categorias = Category.objects.all()
    product =Product.objects.get(ProductId=id)

    datos ={
        'form': ProductForm(instance=product)
    }
    if request.method == 'POST': 
        formulario = ProductForm(request.POST,request.FILES, instance = product)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('watch')
    return render(request, 'u_product.html', datos)

def delete (request, id):
    instance = Product.objects.get(ProductId=id)
    instance.delete()
    return redirect('watch')
