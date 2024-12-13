from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import *
from .serializers import *


# Create your views here.
class GestionViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
class detalleFormularioAViewSet(viewsets.ModelViewSet): 
    queryset = detalleFormularioA.objects.all() 
    serializer_class = detalleFormularioASerializer  # Corregido aquí

class detalleFormularioBViewSet(viewsets.ModelViewSet): 
    queryset = detalleFormularioB.objects.all() 
    serializer_class = detalleFormularioBSerializer
