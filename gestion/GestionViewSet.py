from rest_framework import viewsets
from .models import *
from .serializers import *

class InicioViewSet(viewsets.ModelViewSet):
    queryset = Inicio.objects.all()
    serializer_class = InicioSerializer

class FiltroViewSet(viewsets.ModelViewSet):
    queryset = Filtro.objects.all()
    serializer_class = FiltroSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ContribuyenteViewSet(viewsets.ModelViewSet):
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer

class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

class detalleFormularioAViewSet(viewsets.ModelViewSet):
    queryset = detalleFormularioA.objects.all()
    serializer_class = detalleFormularioASerializer

class detalleFormularioBViewSet(viewsets.ModelViewSet):
    queryset = detalleFormularioB.objects.all()
    serializer_class = detalleFormularioBSerializer
