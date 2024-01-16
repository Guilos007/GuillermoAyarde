from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Curso)
admin.site.register(models.CursoEstudiantes)
admin.site.register(models.Estudiante)
admin.site.register(models.Profesor)