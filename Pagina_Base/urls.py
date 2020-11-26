from django.urls import path

from . import views

app_name = 'Pagina_Base'

urlpatterns = [
    path('', views.index, name='index'),

    
    path('Client/add', views.Create_Client, name='Create_Client'),
    path('Client/List', views.List_Client, name='List_Client'),
    path('Client/Edit<int:pk>', views.Edit_Client, name='Edit_Client'),
    path('Client/Delete<int:pk>', views.Delete_Client, name='Delete_Client'),

    path('Machine/add', views.Create_Machine, name='Create_Machine'),
    path('Machine/list', views.List_Machine, name='List_Machine'),
    path('Machine/Edit<int:pk>', views.Edit_Machine, name='Edit_Machine'),
    path('Machine/Edit_Status<int:pk>', views.Edit_Machine_status, name='Edit_Machine_status'),
    path('Machine/Delete<int:pk>', views.Delete_Machine, name='Delete_Machine'),


    path('Rent/add', views.Rent_Machine, name='Rent_Machine'),
    path('Rent/list', views.List_Rent, name='List_Rent'),
    path('Rent/Edit<int:pk>', views.Edit_Rent, name='Edit_Rent'),



]