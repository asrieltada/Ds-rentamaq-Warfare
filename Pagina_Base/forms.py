from django import forms
from django.shortcuts import render , redirect, get_object_or_404
from bootstrap_datepicker_plus import DatePickerInput ,DateTimePickerInput
from .models import *

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


class Machine_DSWF(forms.Form):
    Machine_ID_Code = forms.CharField(label='Id de la maquina externo')
    Patent = forms.CharField(label='Patente')
    Device_Type = forms.ChoiceField(label='Tipo de Maquina',choices = Machine_Type_types)
    Date_Buy = forms.DateTimeField(label='Fecha de adquisicion', widget=DateTimePickerInput(format='%d/%m/%Y %H:%M'))
    

    Status_Machine_Code = forms.ChoiceField(label='Codigo de estado',choices = Status_code_types)
    Date_Last_Maintenance = forms.DateTimeField(label='Fecha de ultima mantencion',widget=DateTimePickerInput(format='%d/%m/%Y %H:%M'))
    Time_Usage =  forms.IntegerField(label='Tipo de uso')
    Maintenance_Time_Program = forms.DateTimeField(label='echa de proxima mantencion',widget=DateTimePickerInput(format='%d/%m/%Y %H:%M'))
    Status_Description = forms.CharField(label='Descripcion del estado',widget=forms.Textarea)

    def save(self):
        create_status = Status_DSW(Status_Machine_Code=self.cleaned_data.get('Status_Machine_Code') , Date_Last_Maintenance=self.cleaned_data.get('Date_Last_Maintenance') , Time_Usage=self.cleaned_data.get('Time_Usage') , Maintenance_Time_Program=self.cleaned_data.get('Maintenance_Time_Program'), Status_Description=self.cleaned_data.get('Status_Description'))
        create_Machine = Machine_DSW(Machine_ID_Code=self.cleaned_data.get('Machine_ID_Code') , Patent=self.cleaned_data.get('Patent') , Device_Type=self.cleaned_data.get('Device_Type') , Date_Buy=self.cleaned_data.get('Date_Buy') , Status_Device=create_status)
        create_status.save()
        create_Machine.save()

class Status_Editor(forms.ModelForm):
    class Meta:
        model = Status_DSW
        fields = ['Status_Machine_Code','Date_Last_Maintenance', 'Time_Usage','Maintenance_Time_Program','Status_Description']
        widgets = {'Date_Last_Maintenance': DateTimePickerInput(format='%d/%m/%Y %H:mm'),'Maintenance_Time_Program':DateTimePickerInput(format='%d/%m/%Y %H:mm'),'Status_Description':forms.Textarea}
        labels = {
            "Status_Machine_Code": "Codigo de estado",
            "Date_Last_Maintenance": "Fecha de ultima mantencion",
            "Time_Usage": "Tipo de uso",
            "Maintenance_Time_Program": " Fecha de proxima mantencion ",
            "Status_Description": "Descripcion del estado",
        }

class Machine_Editor(forms.ModelForm):
    class Meta:
        model = Machine_DSW
        fields = ['Machine_ID_Code','Patent', 'Device_Type','Date_Buy']
        widgets = {'Date_Buy': DateTimePickerInput(format='%d/%m/%Y %H:mm'),}
        labels = {
            "Machine_ID_Code": "Id de la maquina externo",
            "Patent": "Patente",
            "Device_Type": "Tipo de Maquina",
            "Date_Buy": " Fecha de adquisicion ",
            

        }

class Client_DSWF(forms.ModelForm):
    class Meta:
        model = Client_DSW
        fields = ['name', 'rut','direction','phone','email']
        labels = {
            "name": "Nombre de la empresa",
            "rut": "Rut",
            "direction": "Direccion",
            "phone": " Telefono ",
            "email": "Email"
        }
        

class Rent_Machine_DSWF(forms.ModelForm):
    class Meta:
        model = Rent_Machine_DSW
        fields = ['Machine_ID_Code', 'Client_ID_Code','Date_To_Rent','Time_Usage','Date_To_Return']
        widgets = {'Date_To_Rent': DateTimePickerInput(format='%d/%m/%Y %H:mm'),'Date_To_Return': DateTimePickerInput(format='%d/%m/%Y %H:mm'),}
        labels = {
            "Machine_ID_Code": "Id de la maquina",
            "Client_ID_Code": "Id de la Cliente",
            "Date_To_Rent": "Fecha a arrendar",
            "Time_Usage": " Telefono ",
            "Date_To_Return": "Fecha estimada de retorno"
        }


