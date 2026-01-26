from django.shortcuts import render
from .models import Product

def main_page(request):
    product = Product.objects.all()
    
    context = {
        'products': product
    }

    return render(request, "index.html", context)
