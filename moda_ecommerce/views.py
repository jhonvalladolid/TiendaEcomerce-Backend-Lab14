# moda_ecommerce/views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Categoria, Producto, Cliente, Venta
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, VentaSerializer

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

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': {'id': user.id, 'username': user.username, 'email': user.email}})
    else:
        return Response({'error': 'Invalid Credentials'}, status=400)
