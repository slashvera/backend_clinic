from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Specialty(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'specialty'

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"

class Patients(models.Model):
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
        db_table ='patients'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Doctors(models.Model):
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
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctors')

    especialidad = models.ForeignKey('Specialty', on_delete=models.PROTECT, related_name='doctors')
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES, default='DNI')
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    numero_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'doctors'

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Treatments(models.Model):
    especialidad = models.ForeignKey('Specialty', on_delete=models.PROTECT, releated_name='treatments')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_horas = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    class Meta: 
        db_table = 'treatments'

    def __str__(self):
        return self.nombre

class Appointments(models.Model):
    STATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No asistió'),
    ]

    token = models.CharField(max_length=50, unique=True)
    paciente = models.ForeignKey(Patients, on_delete=models.PROTECT, related_name='appointments')
    doctor = models.ForeignKey(Doctors, on_delete=models.PROTECT, related_name='appointments')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices = STATUS_CHOICES, default='PENIENTE')
    observacion = models.TextField( blank=True)

    def __str__(self):
        return (
            f"Cita {self.token} - "
            f"{self.paciente} - "
            f"{self.fecha} {self.hora}")