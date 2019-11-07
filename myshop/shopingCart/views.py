from django.shortcuts import redirect, HttpResponse
from django.views import generic
from .models import ShopingCart
from product.models import Product


class ShopingCartView(generic.ListView):
    template_name = 'shoping_cart.html'
    context_object_name = 'buyed_product_list'

    def get_queryset(self):
        list_product_ids = ShopingCart.objects.get(id=1).get_list_product_ids()
        product_list = []
        for product_id in list_product_ids:
            product_list.append(Product.objects.get(id=product_id))
        
        return product_list


def add_to_shoping_cart(request, product_id):
    ShopingCart.objects.get(id=1).add_product_id(product_id)
    return redirect('/products')
    # return HttpResponse("lel")
