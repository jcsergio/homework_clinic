from django.urls import path
from AppCoder.views import *


urlpatterns=[
   
    path("", inicio),

    path('main_hospital/', main_hospital, name="main_hospital"),
    
    

    path('enfermera/', enfermera, name="enfermera"),
    path('doctor/', doctor, name="doctor"),
    path('paciente/', paciente, name="paciente"),
    path('busquedaPaciente/', busquedaPaciente, name="busquedaPaciente"),
    path('buscar/', buscar, name="buscar"),

]