from django.db import models


class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)
# fin class Curso

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido
# fin class Estudiante


class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido
# fin class Profesor

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entregable= models.DateField()
    entregado= models.BooleanField()


class Temporal(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=50)


class Data(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    especialidad=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido



class Enfermera(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+" "+self.apellido


class Doctor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    especialidad=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.especialidad

class Paciente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()
    
    def __str__(self):
        return self.nombre+" "+self.apellido





