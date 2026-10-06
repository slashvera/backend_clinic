from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from main.models import Especialidad, Paciente, Doctor, Tratamiento, Cita, Cita_Tratamiento, Consulta_Historial, Ajuste
from serializers import DoctorSerializer, EspecialidadSerializer, PacienteSerializer, TratamientoSerializer, CitaSerializer, Cita_TratamientoSerializer, Consulta_HistorialSerializer, AjusteSerializer

#¿Qué es ModelViewSet?
#Un ModelViewSet es una clase proporcionada por Django REST Framework que combina la funcionalidad de un ViewSet con la de un modelo específico. Permite crear automáticamente vistas para operaciones CRUD (Crear, Leer, Actualizar, Eliminar) basadas en un modelo de Django, simplificando el proceso de desarrollo de API RESTful.


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class CitaViewset(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class Cita_TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Cita_Tratamiento.objects.all()
    serializer_class = Cita_TratamientoSerializer

class Consulta_HistorialViewSet(viewsets.ModelViewSet):
    queryset = Consulta_Historial.objects.all()
    serializer_class = Consulta_HistorialSerializer

class AjusteViewSet(viewsets.ModelViewSet):
    queryset = Ajuste.objects.all()
    serializer_lass = AjusteSerializer
