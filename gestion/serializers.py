from rest_framework import serializers
from .models import Inicio, Filtro, Persona, Contribuyente, Formulario, detalleFormularioA, detalleFormularioB

class InicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inicio
        fields = '__all__'

class FiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filtro
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__'

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'

class detalleFormularioASerializer(serializers.ModelSerializer):
    class Meta:
        model = detalleFormularioA
        fields = '__all__'

class detalleFormularioBSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalleFormularioB
        fields = '__all__'
