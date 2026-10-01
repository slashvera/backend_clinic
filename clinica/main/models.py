from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
        return f"{self.usuario.first_name} {self.usuario.last_name}"


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

    especialidad = models.ForeignKey('Especialidad', on_delete=models.PROTECT, related_name='doctors')
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