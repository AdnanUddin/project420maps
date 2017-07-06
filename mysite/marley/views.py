from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Map, Buyer, Seller



# Create your views here.

def index(request):
    # map_list = Map.objects.first()
    context = {'map_list' : 'placeholder for maps'}
    return render(request, 'marley/index.html')

class BuyerView(generic.FormView):
    model = Buyer
    template_name = 'marley/buyer.html'

class SellerView(generic.FormView):
    model = Seller
    template_name = 'marley/seller.html'

def transaction(request, transaction_id ):
    return None
