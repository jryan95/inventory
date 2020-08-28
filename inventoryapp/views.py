from django.shortcuts import render

# Create your views here.
def index(request):
    """ Homepage for Scentsy Inventory. """
    return render(request, 'inventoryapp/index.html')