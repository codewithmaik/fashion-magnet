from django.shortcuts import render

def index(request):
    ''' A view to render the index template '''
    return render(request, 'home/index.html')
