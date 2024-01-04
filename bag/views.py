from django.shortcuts import render, redirect, reverse

def view_bag(request):
    ''' A view to render the shopping bag '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' A view to add the quantity of the selected product to the shopping bag '''

    # Get the quantity input from the form and convert it into an integer since it will come as a string
    quantity = int(request.POST.get('quantity'))

    # Get the redirect url from the form in order to know where to redirect as soon as the process is finished
    redirect_url = request.POST.get('redirect_url')

    # Set size to None and check if the selected product has a size, if so, set it to the selected size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Set bag variable equal to current value in the session if it already exists, setting it equal to an empty dictionary otherwise
    bag = request.session.get('bag', {})

    # Check if selected item has a size
    if size:
        # Check if selected item exists in bag
        if item_id in list(bag.keys()):
            # Check if selected product with specified size already exists in bag
            if size in bag[item_id]['item_by_size'].keys():
                # Increase quantity of selected item and specified size
                bag[item_id]['item_by_size'][size] += quantity
            else:
                # Update quantity of existing entry with specified size
                bag[item_id]['item_by_size'][size] = quantity
        else:
            # Create new entry for the item as a dictionary in case user selects same item with multiple sizes
            bag[item_id] = { 'item_by_size': { size: quantity }}

    else:
        # Check if selected item exists in the bag
        if item_id in list(bag.keys()):
            # Increase quantity for the existing item in the bag
            bag[item_id] += quantity
        else:
            # Create new entry for the selected item with the specified quantity
            bag[item_id] = quantity
    
    # Override the bag variable into the current session
    request.session['bag'] = bag

    # Print statement for testing 
    # print(request.session['bag'])


    # Return to the redirect url that we got earlier in the view
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    ''' A view to adjust the quantity of the selected product in the shopping bag '''

    # Get the quantity input from the form and convert it into an integer since it will come as a string
    quantity = int(request.POST.get('quantity'))

    # Set size to None and check if the selected product has a size, if so, set it to the selected size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Set bag variable equal to current value in the session if it already exists, setting it equal to an empty dictionary otherwise
    bag = request.session.get('bag', {})

    # Check if selected item has a size
    if size:
        if quantity > 0:
            # Look for item in specified size in the bag and adjust its quantity.
            bag[item_id]['item_by_size'][size] = quantity
        else:
            # Delete item with specified size in the bag.
            del bag[item_id]['item_by_size'][size]
    else:
        if quantity > 0:
            # Look for item in the bag and adjust its quantity.
            bag[item_id] = quantity
        else:
            # Remove item from the bag.
            bag.pop(item_id)
    
    # Override the bag variable into the current session
    request.session['bag'] = bag

    # Print statement for testing 
    # print(request.session['bag'])


    # Return to the redirect url that we got earlier in the view
    return redirect(reverse('view_bag'))