from django.shortcuts import get_object_or_404
from boats.models import Boats


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    boat_count = 0
    
    for id, quantity in cart.items():
        boat = get_object_or_404(Boats, pk=id)
        total += quantity * boat.price
        boat_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'boat': boat})
    
    return {'cart_items': cart_items, 'total': total, 'boat_count': boat_count}