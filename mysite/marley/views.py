from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Map, Buyer



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'marley/index.html'
    context_object_name = 'buyer_list'
    def get_queryset(self):
        return Buyer.objects.all()
    # return render(request, 'marley/index.html')

class BuyerView(generic.FormView):
    model = Buyer
    template_name = 'marley/buyer.html'

def transaction(request, transaction_id ):
    return None
