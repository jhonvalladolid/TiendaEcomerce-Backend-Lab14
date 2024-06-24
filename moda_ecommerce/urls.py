# moda_ecommerce/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ClienteViewSet, VentaViewSet, login_view

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]
