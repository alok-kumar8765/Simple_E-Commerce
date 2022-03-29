from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
import datetime

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {"category": category, "categories": categories, "products": products}
    return render(request, "product_list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {"product": product, "cart_product_form": cart_product_form,"status_code":200}

    return render(request, "product_detail.html", context)

def create_category(request,*args,**kwargs):
    if request.method=="POST":
        name=request.POST.get("name")
        slug=request.POST.get("slug")
        created_at = request.POST.get("created_at")
        updated_at = request.POST.get("updated_at")
        category=Category(name=name,slug=slug,created_at=created_at,updated_at=updated_at)
        category.save()

def create_product(request,*arge,**kwargs):
    if request.method=="POST":
        print(request.data)
        name=request.POST.get("name")
        slug=request.POST.get("slug")
        description = request.POST.get("description")
        price = request.POST.get("price")
        available = request.POST.get("available")
        stock = request.POST.get("stock")
        created_at = request.POST.get("created_at")
        updated_at = request.POST.get("updated_at")
        category= request.POST.get("category")
        product = Product(name=name,slug=slug,description=description,price=price,available=available,stock=stock,created_at=created_at,updated_at=updated_at,category=category)
        product.save()
        # return render

        

