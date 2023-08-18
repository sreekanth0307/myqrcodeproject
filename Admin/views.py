from django.shortcuts import render,redirect
from client.models import *

def Adminlogin(request):
    if request.method=='GET':
        return render(request,'adminlogin.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')  
        error_message=None
        if email=='admin@gmail.com' and password=='admin@123':
            return render(request,'adminhome.html')
        else:
            error_message='invalid username or password'
            return render(request,'adminlogin.html',{'error':error_message})  
def Adminhome(request):
    if request.method=='GET':
        return render(request,'adminhome.html')    
    return redirect(request,'adminhome.html')
def clientapproval(request):
     if request.method=='GET':
         client_obj=Client.objects.all()
         return render(request,'clientapproval.html',{'client_obj':client_obj})
     return redirect(request,'clientapproval.html')
def clientapproval1(request,pk):
    if request.method=='GET':
        client_obj=Client.objects.filter(id=pk)
        for i in client_obj:
            i.status=True
            i.save()
            client_obj=Client.objects.all()
            return render(request,'clientapproval.html',{'client_obj':client_obj})
def clientdecline(request,pk):
    if request.method=='GET':
        client_obj=Client.objects.filter(id=pk)
        for i in client_obj:
            i.status=False
            i.save()
            client_obj=Client.objects.all()
            return render(request,'clientapproval.html',{'client_obj':client_obj})        
# Create your views here.
