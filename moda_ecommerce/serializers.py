# moda_ecommerce/serializers.py
from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Venta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)  # Anidamos el serializador de Categoría para mostrar todos sus detalles
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria', write_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'categoria_id', 'imagen']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion']

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)  # Anidamos el serializador de Cliente para mostrar todos sus detalles
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente', write_only=True)
    producto = ProductoSerializer(read_only=True)  # Anidamos el serializador de Producto para mostrar todos sus detalles
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'cliente_id', 'producto', 'producto_id', 'cantidad', 'precio_total', 'fecha_venta']
