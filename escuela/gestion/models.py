from django.db import models



class Curso(models.Model):
    nombre_curso = models.CharField(max_length=45)
    turno = models.CharField(max_length=45)
    preceptor = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_curso
    


class Alumno(models.Model):
    nombre = models.CharField(max_length=1000)
    apellido = models.CharField(max_length=1000)
    dni_alumno = models.CharField(max_length=8)
    edad = models.CharField(max_length=2)
    gmail = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    id_curso_alumno=models.ForeignKey(Curso,on_delete=models.CASCADE) 

    def __str__ (self):
        return f"{self.nombre} {self.apellido}"
    