from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        """
        Check quantity selected <= quantity in the stock.
        If the above is true then add to cart,
        else print quantity exceeded and return status code 400 
        """
        # cart.add(product)
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    # return redirect('cart:cart_detail')
    return render(request,"product_list.html",status=302,)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    """
    Write a piece of code that will remove 
    the item from the cart.
    """
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    """
    Write a piece of code that will show 
    the item details in the cart.
    """
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    # coupon_apply_form = CouponApplyForm()
    # return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})
    return render(request,'product_list.html',status=200)
