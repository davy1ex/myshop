# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect, HttpResponse

from product.models import Product
# db with login user from social
from django.contrib.auth import logout

from django.shortcuts import render
from social_django.models import UserSocialAuth


# class IndexView(TemplateView):    
#     template_name = 'main/index.html'
#     context_object_name = "user"

#     def get_queryset(self):
#         # user = UserSocialAuth.objects.all()
#         meta = request.session[0]

def index(request):
    # print("\n\n", request.user.is_authenticated)
    if request.user.is_authenticated:
        user = UserSocialAuth.objects.get(id=request.session['_auth_user_id'])
    else:
        user = ''
    return render(request, "main/index.html", {"user": user})

def logout_view(request):
    logout(request)
    return redirect('/')

