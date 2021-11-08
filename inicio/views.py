from django.shortcuts import render
from django.http import HttpResponse
from ferias.models import Producto

def index(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'index.html', context)
