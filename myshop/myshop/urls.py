from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import TemplateView
# from myshop.views import IndexView
import myshop.views 
from product.views import ProductsView
import shopingCart.views

SOCIAL_AUTH_URL_NAMESPACE = 'social'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(template_name="main/index.html")),
    path('', myshop.views.index, name='main'),
    path('products/', ProductsView.as_view(template_name="products/products.html"), name="products"),
    url('', include('social_django.urls', namespace='social')),
    url('logout/', myshop.views.logout_view, name='logout'),
    url('shoping_cart/main/', shopingCart.views.ShopingCartView.as_view(template_name="shoping_cart/shoping_cart.html"), name="shoping_cart"),
    path('shoping_cart/add_<int:product_id>/', shopingCart.views.add_product),
    path('shoping_cart/remove_<int:product_id>/', shopingCart.views.remove_product),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
