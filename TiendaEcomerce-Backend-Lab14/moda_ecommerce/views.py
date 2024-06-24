# moda_ecommerce/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Venta
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, VentaSerializer


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
