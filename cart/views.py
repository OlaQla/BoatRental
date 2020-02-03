from django.shortcuts import render, redirect, reverse
from datetime import datetime

def view_cart(request):
    """Cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    startDay = datetime.strptime(request.POST.get('startDay'), "%Y-%m-%d")
    endDay = datetime.strptime(request.POST.get('endDay'), "%Y-%m-%d")
    quantity = abs((endDay - startDay).days)
  

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('boats'))


def remove_from_cart(request, id):
    """ Remove item from cart """
    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
