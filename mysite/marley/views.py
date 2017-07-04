from django.shortcuts import render
from django.http import HttpResponse

from .models import Map



# Create your views here.

def index(request):
    # map_list = Map.objects.first()
    context = {'map_list' : 'placeholder for maps'}
    return render(request, 'marley/index.html')