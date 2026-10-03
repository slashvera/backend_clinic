from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'especialidades'

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"

class Paciente(models.Model):
    GENDER_CHOICES = [
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro')
    ]

    DOCUMENT_TYPE_CHOICES = [
        ('DNI','Cedula'),
        ('PAS','Pasaporte'),
        ('O','Otro')
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=3, choices=DOCUMENT_TYPE_CHOICES,default='DNI') 
    numero_documento = models.CharField(max_length=20,unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices= GENDER_CHOICES, null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    grupo_sanguineo = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, null=True, blank=True)
    enfermedades = models.TextField(blank=True)
    antecedentes = models.TextField(blank=True)
    odontograma = models.JSONField(default=dict, blank=True)
    contacto_emergencia = models.TextField(max_length=50, blank=True)
    observaciones = models.TextField(blank=True)
    #Conectamos el modeleo de usuario Django on el modelo pacientes
    #usuario =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='pacientes')
    class Meta:
        db_table ='pacientes'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Doctor(models.Model):
    GENDER_CHOICES = [
            ('M','Masculino'),
            ('F','Femenino'),
            ('O','Otro')
        ]

    DOCUMENT_TYPE_CHOICES = [
        ('DNI','Cedula'),
        ('PAS','Pasaporte'),
        ('O','Otro')
    ]

    #Conetamos el modelo de usuario Django con el modelo doctores
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')

    especialidad = models.ForeignKey('Especialidad', on_delete=models.PROTECT, related_name='doctor')
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES, default='DNI')
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    numero_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'doctores'

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Tratamiento(models.Model):
    especialidad = models.ForeignKey('Especialidad', on_delete=models.PROTECT, related_name='tratamientos')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_minutos = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    class Meta: 
        db_table = 'tratamientos'

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    STATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No asistió'),
    ]

    token = models.CharField(max_length=50, unique=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices = STATUS_CHOICES, default='PENDIENTE')
    observacion = models.TextField( blank=True)

    class Meta:
        db_table = 'citas'

    def __str__(self):
        return (
            f"Cita {self.token} - "
            f"{self.paciente} - "
            f"{self.fecha} {self.hora}")

class Cita_Tratamiento(models.Model):
    cita = models.ForeignKey( Cita, on_delete=models.CASCADE, related_name='tratamientos')
    tratamiento = models.ForeignKey( Tratamiento, on_delete=models.PROTECT, related_name='citas')
    precio = models.DecimalField( max_digits=10, decimal_places=2)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cita', 'tratamiento'],
                name='unique_cita_tratamiento'
            )
        ]

    def __str__(self):
        return f"{self.cita} - {self.tratamiento}"

class Consulta_Historial(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, related_name='historial')
    motivo_consulta = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    fecha_registro = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"Consulta - {self.cita.paciente}"

class Ajuste(models.Model):

    nombre_clinica = models.CharField(max_length=150)
    descripcion_clinica = models.TextField(blank=True)
    direccion = models.TextField(blank=True)

    telefono = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)
    divisa = models.CharField(max_length=10,default='USD')
    logo = models.CharField(max_length=255,blank=True)
    web = models.URLField(blank=True)

    def __str__(self):
        return self.nombre_clinica