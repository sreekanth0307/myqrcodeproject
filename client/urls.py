
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('base',views.base,name='base'),
    path('clientregister',views.clientregister,name='clientregister'),
    path('clientlogin',views.clientlogin,name='clientlogin'),
    path('clientsignup',views.clientsignup,name='clientsignup'),
    path('clienthome',views.clienthome,name="clienthome"),
    path('clientdata',views.clientdata,name="clientdata"),
    path('clientadminmsg',views.clientadminmsg,name="clientadmin"),
    path('downloaded',views.downloaded,name="downloaded"),
    path('logoutclient',views.logoutclient,name='logoutclient'),
    path('adminhome',views.adminhome,name='adminhome'),
    #path('clientlogin',views.clientlogin,name="clientlogin")
]