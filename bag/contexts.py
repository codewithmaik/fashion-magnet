from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    # Set bag variable equal to current value in the session if it already exists, setting it equal to an empty dictionary otherwise
    bag = request.session.get('bag', {})

    # Get product for every item in bag, calculate the total price and increase the product count
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            # Add object to list of items to access it all over the application
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['item_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                # Add object to list of items to access it all over the application
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                    })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context