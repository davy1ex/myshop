from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

from product.models import Product


class ProductsView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()