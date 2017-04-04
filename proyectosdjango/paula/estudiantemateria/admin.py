from django.contrib import admin

# Register your models here.
from estudiantemateria.models import Estudiante, Materia

admin.site.register(Estudiante)
admin.site.register(Materia)

