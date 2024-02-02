from django.shortcuts import render,redirect,get_object_or_404
from projectapp .models import Product,Details
from . models import Cartpage
from . models import Order

from django.contrib import messages

# Create your views here.
def cart(request,id):
    
    product = Product.objects.get(id=id)
    user_id=None
    try:
        user_id = request.session['user']
    except:
        return redirect('credential:login')
    try:
        cartitem = Cartpage.objects.get(product=product)
        if cartitem.quantity < cartitem.product.stock:
            cartitem.quantity += 1
            cartitem.save()
    except Cartpage.DoesNotExist: 
        cartitem = Cartpage(product=product, user_id=user_id, quantity=1)
        cartitem.save()

    
    return redirect('cart:display')


def display(request):
    user_id = request.session.get('user', None)
    detail=Details.objects.all()
    data = Cartpage.objects.all().filter(user_id=user_id)
    
    total_amount = sum(item.product.price * item.quantity for item in data)

    return render(request, 'cart.html', {'cart': data,"total_amount": total_amount,"addr":detail})

def delete(request,id):
    user_id = request.session['user']
    product=Product.objects.get(id=id)
    categoty=Cartpage.objects.get(product=product,user_id=user_id)
    categoty.delete()
   
    return redirect('cart:display')

def dele(request,id):
    
    user_id = request.session['user']
    product=Product.objects.get(id=id)
    cartitem = Cartpage.objects.get(product=product,user_id=user_id)
    if cartitem.quantity >1:
            cartitem.quantity -= 1
            cartitem.save()
    return redirect('cart:display')

def buy(request):
    selected_address = request.GET.get('selected_address')

    if selected_address:
        cart_items = Cartpage.objects.all()

        for cart_item in cart_items:
            if cart_item.product.stock >= cart_item.quantity:
                cart_item.product.stock -= 1
                cart_item.product.save()
                order = Order(quantity=cart_item.quantity, product=cart_item.product, address=selected_address)
                order.save()
                cart_item.delete()
            else:
                return redirect('cart:display')

        return redirect('/')
    else:
        return render(request, 'cart.html')

def order_details(request):
    user_id = request.session.get('user', None)
    orders = Order.objects.filter(user_id=user_id)
    
    return render(request, 'order_details.html', {'orders': orders})