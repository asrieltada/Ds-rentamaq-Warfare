from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import SetPasswordForm , AuthenticationForm , UserChangeForm , UserCreationForm
from .forms import updateForm
from django.contrib.auth.models import User,Group
from django.contrib import messages


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
        else:
            print("usuario no creado")
            messages.error(request, 'Algunos de los campos no están correctos. Por favor, verifique los datos y vuelva a intentarlo.')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def ChangePassword(request):
    messages.warning(request, 'Se editara la contraseña del Usuario:')
    userCh = User.objects.get(username=request.user.username)
    print (userCh.id)
    print(request.method)
    if request.method == 'POST':
        form = SetPasswordForm(userCh, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Tu contraseña se actualizó correctamente!')
            return redirect('user:Profile')
        else:
            messages.error(request, 'Uuuy tenemos un error.')
    else:
        form = SetPasswordForm(userCh)
    return render(request, 'users/ChangePassword.html', {
        'form': form
    })


def Profile(request):
    if request.user.is_authenticated:
        template = 'users/Profile.html'
        userrr = get_object_or_404(User, username=request.user.username)
        context = {"Userr": userrr}
        return render(request, template, context)
    else:    
        return render(request,'users/Profile.html',)

def EditUser(request):
    messages.warning(request, 'Se editara al Usuario: ')

    form = updateForm (instance = request.user)
    if request.method == 'POST':
        form = updateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos se han actualizado correctamente!')
            return redirect('user:Profile')
        else:
            messages.error(request, 'Uuuy tenemos un error.')
            
    return render(request,'users/EditUser.html',{'form':form})



def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                messages.success(request, 'Inicio de sección correctamente '+ user.username +'!')
                # Y le redireccionamos a la portada
                return redirect('/logon')
        else:
            messages.error(request, 'Usuario/Contraseña incorrecto, Por favor reintente')
    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

