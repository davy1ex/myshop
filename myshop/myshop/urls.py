from django.contrib import admin
from django.urls import path
# from django.views.generic import TemplateView
from product.views import ProductsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductsView.as_view(template_name="products.html"), name="products"),
]
