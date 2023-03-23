from django.shortcuts import render
from django.views import View
# from products.models import Product
# Create your views here.


class IndexView(View):

    def get(self, request):
        products = {}

        return render(request, "index.html", {'products': products})
