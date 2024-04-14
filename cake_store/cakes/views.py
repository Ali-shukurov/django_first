from django.shortcuts import render, HttpResponse
from .models import Cake
# Create your views here.

def home_page(request):
    cakes = Cake.objects.all()
    data = {
        'tortlar': cakes
    }
    return render(request, 'cakes/home.html', data)

def index_page(request):
    return HttpResponse('index')

def cake_details(request, pk):
    cake = Cake.objects.get(id=pk)
    data = {
        'tort': cake 
    }
    return render(request, 'cakes/cake_details.html', data)
