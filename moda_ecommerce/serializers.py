# moda_ecommerce/serializers.py
from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Venta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion']

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    producto = ProductoSerializer()

    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'producto', 'cantidad', 'precio_total', 'fecha_venta']
