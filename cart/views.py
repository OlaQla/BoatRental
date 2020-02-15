from django.shortcuts import render, redirect, reverse
from datetime import datetime

def view_cart(request):
    """Cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    startDay = datetime.strptime(request.POST.get('startDay'), "%Y-%m-%d")
    endDay = datetime.strptime(request.POST.get('endDay'), "%Y-%m-%d")
    quantity = abs((endDay - startDay).days) + 1
  
    cart = request.session.get('cart', {})
    current = cart.get(id, [])
    current.append((startDay.strftime("%Y-%m-%d"), endDay.strftime("%Y-%m-%d"), quantity))
    cart[id] = current

    request.session['cart'] = cart
    return redirect(reverse('boats'))


def remove_from_cart(request, id, subid):
    """ Remove item from cart """
    cart = request.session.get('cart', {})
    current = cart.get(id)
    if(len(current) == 1): 
        cart.pop(id)
    else:
        del current[int(subid)]
        cart[id] = current

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
