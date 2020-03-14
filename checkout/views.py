from django.shortcuts import render, get_object_or_404, reverse, redirect
import stripe
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from .models import OrderLineItem
from boats.models import Boats
from datetime import datetime

stripe.api_key = settings.STRIPE_SECRET

# Try to make a checkout with POSTed data
@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        # Proceed only if data from form is valid
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()

            # Save an order
            order.save()

            # Get cart object
            cart = request.session.get('cart', {})
            total = 0
            for id, boat_orders in cart.items():
                boat = get_object_or_404(Boats, pk=id)

                # Calculate details and create order lines for each boat in a checked out basket
                for individual_order in boat_orders:
                    quantity = individual_order[2]
                    total += quantity * boat.price
                    order_line_item = OrderLineItem(
                        user=request.user,
                        order=order,
                        boat=boat,
                        quantity=quantity,
                        subtotal=quantity * boat.price,
                        from_date=datetime.strptime(
                            individual_order[0],
                            "%Y-%m-%d").timestamp(),
                        to_date=datetime.strptime(
                            individual_order[1],
                            "%Y-%m-%d").timestamp())
                    order_line_item.save()

            # Try charging customer's card using Stripe
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            # If successful show relevant message and redirect user to profile where order should already be visible
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        # It is not a POST request, render checkout forms 
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request,
                  "checkout.html",
                  {"order_form": order_form,
                   "payment_form": payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE})
