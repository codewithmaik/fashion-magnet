from django.shortcuts import render, redirect

def view_bag(request):
    ''' A view to render the shopping bag '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' A view to add the quantity of the selected product to the shopping bag '''

    # Get the quantity input from the form and convert it into an integer since it will come as a string
    quantity = int(request.POST.get('quantity'))

    # Get the redirect url from the form in order to know where to redirect as soon as the process is finished
    redirect_url = request.POST.get('redirect_url')

    # Set bag variable equal to current value in the session if it already exists, setting it equal to an empty dictionary otherwise
    bag = request.session.get('bag', {})

    # Increase the quantity if the item_id already exists in the bag variable, add item_id with its quantity otherwise
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    # Override the bag variable into the current session
    request.session['bag'] = bag

    # Print statement for testing 
    # print(request.session['bag'])


    # Return to the redirect url that we got earlier in the view
    return redirect(redirect_url)
