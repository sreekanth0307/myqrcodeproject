from django.urls import path
from Admin import views
urlpatterns=[
    path('Adminlogin',views.Adminlogin,name='Adminlogin'),
    path('Adminhome',views.Adminhome,name='Adminhome'),
    path('clientapproval',views.clientapproval,name='clientapproval'),
    path('clientapproval1<str:pk>',views.clientapproval1,name='clientapproval1'),
    path('clientdecline<str:pk>',views.clientdecline,name='clientdecline'),
]