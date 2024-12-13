from django.db import models

class Inicio(models.Model):
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario

class Filtro(Inicio):
    numero_filtro = models.SmallIntegerField()
    nota = models.CharField(max_length=255)

class Persona(Inicio):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=13)
    rtn = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    telefono = models.BigIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Contribuyente(Persona):
    numero_expediente = models.IntegerField()

class Formulario(Contribuyente):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    nombre_propietario = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    clave = models.IntegerField()
    area_terreno = models.IntegerField()
    declaracion = models.FileField(upload_to='documentos/')
    croquis = models.FileField(upload_to='documentos/')
    firma = models.FileField(upload_to='documentos/')
    estado_cuenta = models.FileField(upload_to='documentos/')

    def __str__(self):
        return self.nombre_propietario

class detalleFormularioA(Formulario):
    tomo = models.IntegerField()
    numero = models.IntegerField()
    matricula = models.CharField(max_length=50)
    area_terreno_varas = models.IntegerField()
    tipo_obra = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    tipo_inmueble = models.CharField(max_length=50)
    unidades = models.IntegerField()
    metros_cuadrados = models.IntegerField()
    largo = models.IntegerField()
    alto = models.IntegerField()
    profundidad = models.IntegerField()
    area = models.IntegerField()
    costo_obra = models.CharField(max_length=100)
    corte_arbol = models.BooleanField()
    rotura_via = models.BooleanField()
    solvencia = models.FileField(upload_to='documentos/')
    escritura = models.FileField(upload_to='documentos/')
    constitucion_sociedad = models.FileField(upload_to='documentos/')

class detalleFormularioB(Formulario):
    rtn_comercial = models.CharField(max_length=15)
    direccion_proyecto = models.CharField(max_length=100)
    zonificacion = models.CharField(max_length=50)
    actividad_realizar = models.CharField(max_length=50)
    nombre_comercial = models.CharField(max_length=50)
    condiciones_operacion = models.CharField(max_length=50)
    tamanio_obra = models.IntegerField()
    area_util_inmueble = models.IntegerField()
    motivo_solicitud_negocio = models.CharField(max_length=15)
    motivo_solicitud_ambiental = models.CharField(max_length=15)
