from django.contrib import admin
from main.models import Especialidad, Paciente, Doctor, Tratamiento, Cita, Cita_Tratamiento, Consulta_Historial, Ajuste


# Register your models here.
admin.site.site_header = "Administracion Clinica"
admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Tratamiento)
admin.site.register(Cita)
admin.site.register(Cita_Tratamiento)
admin.site.register(Consulta_Historial)
admin.site.register(Ajuste)