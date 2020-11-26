# Proyecto base Django Dockerizado
 Proyecto base para django

## Levantamiento de Django con docker
 Para comenzar a levantar la plataforma necesitas instalar docker hub 
 y en la carpeta que contenga el docker-compose.yml ejecutar el siguiente comando
```
  docker build -t servidor_django:1.2 . 
 
   docker-compose up 
```
y luego para levantar el proyecto se ejecutan los siguientes comandos
```
  docker-compose run web python manage.py makemigrations 
  docker-compose run web python manage.py migrate 
  docker-compose up 
```
## Creacion de proyecto nuevo
 en caso de que requiera ocupar el docker del proyecto para hacer un nuevo proyecto django
```
 docker-compose run web django-admin startproject main .
```
 en caso de inicializar una app dentro del proyecto de django
 
```
 docker-compose run web python manage.py startapp NOMB-APP
```

