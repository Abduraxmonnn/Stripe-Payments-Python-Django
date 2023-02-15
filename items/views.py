# Stripe
import stripe

# Django
from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Project
from .models import Item

def list_items(request):
    items = Item.objects.all()

    contex = {
        'items': items
    }

    return render(request, 'items/list_items.html', contex)


def item_detail(request, pk=None):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Http404

    context = {
        'item': item,
    }
    return render(request, 'items/purchase.html', context)

@csrf_exempt
def create_checkout_session(request, pk=None):
    # if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        product = stripe.Product.create(
            name=Item.objects.get(pk=pk).name,
            description=Item.objects.get(pk=pk).description,
            # images=['https://img.freepik.com/free-photo/close-up-hand-holding-smartphone_23-2149148857.jpg?w=2000'],
        )

        price = stripe.Price.create(
            product=product.id,
            unit_amount=Item.objects.get(pk=pk).price,
            currency=Item.objects.get(pk=pk).currency,
        )

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    }
                ],
                mode='payment',
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
