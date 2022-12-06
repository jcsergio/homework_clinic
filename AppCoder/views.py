from django.shortcuts import render
from .models import Enfermera,Doctor,Paciente
from django.http import HttpResponse

from AppCoder.forms import EnfermeraForm, DoctorForm, PacienteForm
# Create your views here.






# Create your views here.


#-------------------------------------
# New Data (SDA)
# ------------------------------------


def inicio(request):
   # return HttpResponse("Pagina de inicio")
    return render (request, "AppCoder/inicio.html")

def clinica(request):
   # return HttpResponse("Pagina de estudiantes")
   return render (request, "AppCoder/clinica.html")


def prueba(request):
   # return HttpResponse("Pagina de estudiantes")
   return render (request, "AppCoder/prueba.html")


def main_hospital(request):
   # return HttpResponse("Pagina de estudiantes")
   return render (request, "AppCoder/main_hospital.html")


def enfermera(request):
   # return HttpResponse("Pagina de profesores")
   if request.method=="POST":
      form=EnfermeraForm(request.POST)
      if form.is_valid():
         informacion=form.cleaned_data
         print(informacion)
         nombre=informacion["nombre"]
         apellido=informacion["apellido"]
    

         enfermera = Enfermera(nombre=nombre,  apellido=apellido)
         enfermera.save()
         return render (request, "AppCoder/main_hospital.html", {"mensaje": "Enfermera Creada Correctamente!"})
   else:
        formulario=EnfermeraForm()

   return render (request, "AppCoder/enfermera.html", {"form":formulario})


def doctor(request):
   # return HttpResponse("Pagina de profesores")
   if request.method=="POST":
      form=DoctorForm(request.POST)
      if form.is_valid():
         informacion=form.cleaned_data
         print(informacion)
         nombre=informacion["nombre"]
         apellido=informacion["apellido"]
         email=informacion["email"]
         especialidad=informacion["especialidad"]

         doctor = Doctor(nombre=nombre, apellido=apellido, email=email, especialidad=especialidad)
         doctor.save()
         return render (request, "AppCoder/inicio.html", { "mensaje": "Doctor Creado Correctamente!"})
   else:
        formulario=DoctorForm()

   return render (request, "AppCoder/doctor.html", {"form":formulario})



def paciente(request):
   # return HttpResponse("Pagina de profesores")
   if request.method=="POST":
      form=PacienteForm(request.POST)
      if form.is_valid():
         informacion=form.cleaned_data
         print(informacion)
         nombre=informacion["nombre"]
         apellido=informacion["apellido"]
         email=informacion["email"]
         telefono=informacion["telefono"]

         paciente = Paciente(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
         paciente.save()
         return render (request, "AppCoder/inicio.html", {"mensaje": "Paciente Creado Correctamente!"})
   else:
        formulario=PacienteForm()

   return render (request, "AppCoder/paciente.html", {"form":formulario})


def busquedaPaciente(request):
      return render(request, "AppCoder/busquedaPaciente.html")

def buscar(request):
      
    if request.GET["telefono"]:

        telefono=request.GET["telefono"]
        pacientes=Paciente.objects.filter(telefono=telefono)
        return render(request, "AppCoder/resultadosBusqueda.html", {"pacientes":pacientes})
    else:
         return render(request, "AppCoder/busquedaPaciente.html", {"mensaje": "Debe ingresar un telefono"})