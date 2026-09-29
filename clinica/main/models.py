from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pacientes(models.Model):
    GENERO_CHOICES = [
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro')
    ]

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI','Cedula'),
        ('PAS','Pasaporte'),
        ('O','Otro')
    ]

    TIPO_SANGRE_CHOICES = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    ]

    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES,default='DNI') 
    numero_documento = models.CharField(max_length=20,unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices= GENERO_CHOICES, default='O', null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    grupo_sanguineo = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES, null=True, blank=True)
    enfermedades = models.TextField(blank=True)
    antecedentes = models.TextField(blank=True)
    odontograma = models.JSONField(default=dict, blank=True)
    contacto_emergencia = models.TextField(max_length=50, blank=True)
    observaciones = models.TextField(blank=True)

    #Conectamos el modeleo de usuario Django on el modelo pacientes
    usuario =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='pacientes')

    class Meta:
        db_table ='pacientes'

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"


class Doctores(models.Model):
    GENERO_CHOICES = [
            ('M','Masculino'),
            ('F','Femenino'),
            ('O','Otro')
        ]

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI','Cedula'),
        ('PAS','Pasaporte'),
        ('O','Otro')
    ]

    #Conetamos el modelo de usuario Django con el modelo doctores
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctores')
