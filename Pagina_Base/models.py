from django.db import models
from datetime import datetime  
from django.utils import timezone



# Create your models here.

Machine_Type_types = (("I","Cargador Frontal"),
                      ("N","Retro excavadora"),
                      ("G","Bulldozer"),
                      ("E","Camión tolva con gato"),
                      ("S","Tractor con guinche"),
                      ("C","Camión CUNA"),
                    )

Status_code_types = (("A","Activo"),
                      ("R","Reservado"),
                      ("S","Servicio Tecnico"),
                      ("E","De baja"),

                    )

class Status_DSW(models.Model):
    Status_Machine_Code = models.CharField(choices =Status_code_types,default='A',max_length=2)
    Date_Last_Maintenance = models.DateTimeField(null=True, blank=True)
    Time_Usage = models.PositiveIntegerField()
    Maintenance_Time_Program =  models.DateTimeField(null=True, blank=True)
    Status_Description = models.CharField(max_length=500)

class Machine_DSW(models.Model):
    Machine_ID_Code = models.CharField(max_length=100)
    Patent = models.CharField(max_length=100)
    Device_Type = models.CharField(choices = Machine_Type_types, default='C' ,max_length=2)
    Date_Buy = models.DateTimeField(null=True, blank=True)
    Status_Device = models.ForeignKey(Status_DSW, on_delete=models.CASCADE)

class Client_DSW(models.Model):
    name = models.CharField(max_length=150)
    rut = models.CharField(max_length=150)
    direction = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField()

class Rent_Machine_DSW(models.Model):
    Machine_ID_Code = models.ForeignKey(Machine_DSW, on_delete=models.DO_NOTHING)
    Client_ID_Code = models.ForeignKey(Client_DSW, on_delete=models.DO_NOTHING)
    Date_To_Rent = models.DateTimeField(null=True, blank=True)
    Time_Usage = models.PositiveIntegerField(null=True)
    Date_To_Return = models.DateTimeField(null=True, blank=True)
