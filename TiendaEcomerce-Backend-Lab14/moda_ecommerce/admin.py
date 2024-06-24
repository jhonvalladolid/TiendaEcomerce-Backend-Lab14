# moda_ecommerce/admin.py
from django.contrib import admin
from .models import Categoria, Producto, Cliente, Venta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']
    list_filter = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'categoria', 'imagen']
    search_fields = ['nombre', 'categoria__nombre']
    list_filter = ['categoria', 'precio']
    list_editable = ['precio', 'stock']
    list_per_page = 20

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'dni', 'email', 'telefono']
    search_fields = ['nombres', 'apellidos', 'dni', 'email']
    list_filter = ['nombres', 'apellidos']
    list_per_page = 20

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'cantidad', 'precio_total', 'fecha_venta']
    search_fields = ['cliente__nombres', 'cliente__apellidos', 'producto__nombre']
    list_filter = ['fecha_venta']
    list_per_page = 20
