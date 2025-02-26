from django.shortcuts import render
from .models import Product
# Create your views here.


def shop_list_view(request):
    products = Product.objects.all()

    context = {
        'obj_list': products
    }
    return render(request, 'shop/shop.html', context)