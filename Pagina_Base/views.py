from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from .forms import *
from .models import *


def index(request):
    return render(request, "pagina_base/home.html")
# Acciones Cliente
def Create_Client(request):
    template_name = 'pagina_base/Client/Create_Client.html'
    form = Client_DSWF(request.POST,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Pagina_Base:List_Client')
    context = {"form": form}
    return render(request, template_name, context)

def List_Client(request):
    template = 'pagina_base/Client/List_Client.html'
    Client_List = Client_DSW.objects.all()
    context = {"Client_List": Client_List,}
    return render(request, template, context)

def Edit_Client(request, pk):
    template = 'pagina_base/Client/Edit_Client.html'
    Client_one = get_object_or_404( Client_DSW, pk = pk )
    form= Client_DSWF(request.POST or None, instance = Client_one)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('Pagina_Base:List_Client')
    context = {"form": form}
    return render(request, template, context)

def Delete_Client(request, pk):
    template = 'pagina_base/Client/Delete_Client.html'
    client =get_object_or_404(Client_DSW, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('Pagina_Base:List_Client')
    context = {"client": client}
    return render(request, template, context)


# Acciones Maquinas
def Create_Machine(request):
    template = 'pagina_base/Machine/Create_Machine.html'
    form = Machine_DSWF(request.POST,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Pagina_Base:index')
    context = {"form": form}
    return render(request, template, context)

def List_Machine(request):
    template = 'pagina_base/Machine/List_Machine.html'
    Machine_List = Machine_DSW.objects.all()
    Status_List = Status_DSW.objects.all()
    context = {"Machine_List": Machine_List, "Status_List":Status_List }
    return render(request, template, context)

def Edit_Machine(request, pk):
    template = 'pagina_base/Machine/Edit_Machine.html'
    Machine_one = get_object_or_404( Machine_DSW, pk = pk )
    form= Machine_Editor(request.POST or None, instance = Machine_one)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('Pagina_Base:List_Machine')
    context = {"form": form}
    return render(request, template, context)

def Edit_Machine_status(request, pk):
    template = 'pagina_base/Machine/Edit_Machine_status.html'
    Machine_one = get_object_or_404( Machine_DSW, pk = pk )
    Status_one = get_object_or_404( Status_DSW, pk = Machine_one.Status_Device.id )
    form= Status_Editor(request.POST or None, instance = Status_one)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('Pagina_Base:List_Machine')
    context = {"form": form}
    return render(request, template, context)

def Delete_Machine(request, pk):
    template = 'pagina_base/Machine/Delete_Machine.html'
    Machine =get_object_or_404(Machine_DSW, pk=pk)
    if request.method == 'POST':
        Machine.delete()
        return redirect('Pagina_Base:List_Machine')
    context = {"Machine": Machine}
    return render(request, template, context)

#Acciones Renta
def Rent_Machine(request):
    template = 'pagina_base/Rent_a_Machine/Add_Rent.html'
    Machine_List = Machine_DSW.objects.all()
    Status_List = Status_DSW.objects.all()
    Client_List = Client_DSW.objects.all()
    form = Rent_Machine_DSWF(request.POST,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Pagina_Base:List_Rent')
        
    else:
        messages.error(request, 'Algunos de los campos no están correctos. Por favor, verifique los datos y vuelva a intentarlo.')
       
    context = {"Machine_List": Machine_List, "Client_List":Client_List, "Status_List":Status_List ,"form": form,}
    return render(request, template, context)

def List_Rent(request):
    template = 'pagina_base/Rent_a_Machine/List_Rent.html'
    Machine_List = Machine_DSW.objects.all()
    Status_List = Status_DSW.objects.all()
    Client_List = Client_DSW.objects.all()
    Rent_List = Rent_Machine_DSW.objects.all()

  
    context = {"Machine_List": Machine_List, "Client_List":Client_List, "Status_List":Status_List ,"Rent_List": Rent_List,}
    return render(request, template, context)

def Edit_Rent(request, pk):
    template = 'pagina_base/Rent_a_Machine/Edit_Rent.html'
    Machine_List = Machine_DSW.objects.all()
    Status_List = Status_DSW.objects.all()
    Client_List = Client_DSW.objects.all()

    Rent_one = get_object_or_404( Rent_Machine_DSW, pk = pk )

    form= Rent_Machine_DSWF(request.POST or None, instance = Rent_one)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('Pagina_Base:List_Rent')
        
    else:
        context = {"Machine_List": Machine_List, "Client_List":Client_List, "Status_List":Status_List ,"form": form,}
        return render(request, template, context)



