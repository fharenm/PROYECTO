from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'formulario_a', detalleFormularioAViewSet, basename='formulario_a') 
router.register(r'formulario_b', detalleFormularioBViewSet, basename='formulario_b')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs generadas por el router
]
