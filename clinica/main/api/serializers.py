from rest_framework import serializers
from main.models import Especialidad, Paciente, Doctor, Tratamiento, Cita, Cita_Tratamiento, Consulta_Historial, Ajuste
from django.contrib.auth.models import User

#Serializers: Nos permitira convertir Objetos de python a JSON y Viceversa, para poder enviar y recibir datos desde el frontend.
