from django.db import models
from django.core.urlresolvers import reverse

class Estudiante(models.Model):
	nombre1=models.CharField(max_length=100,blank=True)
	nombre2=models.CharField(max_length=100,blank=True)
	apellido1=models.CharField(max_length=100,blank=True)
	apellido2=models.CharField(max_length=100,blank=True)
	semestre=models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.nombre1+" "+self.apellido1

class Materia(models.Model):
	nombre=models.CharField(max_length=100,blank=True)
	profesor=models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.nombre+" "+self.profesor
