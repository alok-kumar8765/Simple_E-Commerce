from multiprocessing import context
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreatedForm
from django.http import HttpResponseRedirect, HttpResponse
from cart.cart import Cart
from shop.models import Product

# from django.contrib.auth.decorators import login_required


def order_create(request):
    cart=Cart(request)
    if request.method == "POST":
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            # cart = Cart(request)
            order = form.save()
            totalprice = 0
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'], quantity=item['quantity'])
            cart.clear()
            """
            Check the total quantity in the cart 
            (totalquantity = sum of all prices of all items in the cart)
            if quantity is 0 then print 'There is no item in the cart' and 
            return response code = 400.
            clear the cart after successfully placing the order
            >> cart.clear()
            """
            return render(request, 'orders/order/create.html', {'order': order},status=400)
            # return render(request, "product_list.html", status=400)
    else:
        form = OrderCreatedForm()
        
        # context = {"form": form, "status_code":200}
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form},status=200)    
