from rest_framework import serializers
from main.models import Especialidad, Paciente, Doctor, Tratamiento, Cita, Cita_Tratamiento, Consulta_Historial, Ajuste
from django.contrib.auth.models import User

#Serializers: Nos permitira convertir Objetos de python a JSON y Viceversa,
#  para poder enviar y recibir datos desde el frontend.
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class TratamientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class CitaSerializers(serializers.ModelSerializer):
    class Meta:
        model: Cita
        fields = '__all__'

class Cita_TratamientoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Cita_Tratamiento
        fields  = '__all__'

class Consulta_HistorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consulta_Historial
        fields = '__all__'

class AjusteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ajuste
        fields = '__all__'
