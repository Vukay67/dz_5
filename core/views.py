from django.shortcuts import render
from .models import Product, Article

def main_page(request):
    product = Product.objects.all()
    
    context = {
        'products': product
    }

    return render(request, "index.html", context)


def article_page(request):
    article = Article.objects.all()

    context = {
        'article': article
    }
    
    return render(request, "article.html", context)
