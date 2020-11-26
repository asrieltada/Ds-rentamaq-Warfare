from django.urls import path

from . import views
app_name = 'user'
urlpatterns = [
    path('logon', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('ChangePassword', views.ChangePassword ,name="ChangePassword"),
    path('Profile' , views.Profile , name="Profile" ),
    path('EditUser',views.EditUser,name="EditUser"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]