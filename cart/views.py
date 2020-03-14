from django.shortcuts import render, redirect, reverse
from boats.models import FeaturedBoat, Boats
from datetime import datetime

# Render cart details page 
def view_cart(request):
    """Cart contents page"""
    featuredBoats = map(lambda fb: fb.boat, FeaturedBoat.objects.all()[:3])
    return render(request, "cart.html", {'featured_boats': featuredBoats})

# Add item to cart
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    startDay = datetime.strptime(request.POST.get('startDay'), "%Y-%m-%d")
    endDay = datetime.strptime(request.POST.get('endDay'), "%Y-%m-%d")
    quantity = abs((endDay - startDay).days) + 1

    # Append item to cart
    cart = request.session.get('cart', {})
    current = cart.get(id, [])
    current.append(
        (startDay.strftime("%Y-%m-%d"),
         endDay.strftime("%Y-%m-%d"),
         quantity))
    cart[id] = current

    # Set new cart contents to object in session
    request.session['cart'] = cart

    # Redirect to page presenting cart contents
    return redirect(reverse('view_cart'))


# View reoving item from cart
def remove_from_cart(request, id, subid):
    # Remove item from cart 
    cart = request.session.get('cart', {})
    current = cart.get(id)
    if(len(current) == 1):
        cart.pop(id)
    else:
        del current[int(subid)]
        cart[id] = current

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Change quantity of item in cart
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
