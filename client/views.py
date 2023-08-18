from django.shortcuts import render,redirect
from client.models import *
from client.utils import render_to_pdf
from io import BytesIO,StringIO
from django.core.files import File
import qrcode
import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def clientregister(request):
    return render(request,'clientregister.html')
def clientlogin(request):
    return render(request,"clientlogin.html")
def clientsignup(request):
    if request.method=="POST":
        clientname=request.POST.get('clientname')
        email=request.POST.get('Email')
        contactno=request.POST.get('ContactNumber')
        pwd=request.POST.get('Pwd')
        Pwd1=request.POST.get('Pwd1')
        adhar=request.POST.get('Adhar')
        photo=request.FILES['Photo']
        client_obj=Client(clientname=clientname,email=email,contactno=contactno,pwd=pwd,adhar=adhar,photo=photo)
        client_obj.save()
        return redirect(clientadminmsg)  
        '''error_message=validateclient(client_obj)
        if not error_message:
            client_obj.save()
            return redirect("Clientchkadminmsg")
        else:
            data={
                'error':error_message,
            }
            return render(request,"clientregister.html")'''
    return render(request,'clientregister.html')
def clienthome(request):
    return render(request,"clienthome.html")
def clientdata(request):
    if request.method=='GET':
        return render(request,"clientdata.html")
    if request.method=="POST":
        #dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        district=request.POST.get('district')
        contry=request.POST.get('country')
        pincode=request.POST.get('pin')
        education=request.POST.get('education')
        print(gender,address,district,contry,pincode,education)
        obj=Clientdata(gender=gender,address=address,district=district,contry=contry,pincode=pincode,education=education,client=Client(request.session['id']))
        obj.save()
        obj1=Client.objects.filter(id=request.session['id'])
        for i in obj1:
            name=i.clientname
            email=i.email
            phone=i.contactno
            adhar=i.adhar

        global pdf
        pdf=render_to_pdf(obj.id,"clientprofilecard.html",{'obj':obj,'obj1':obj1})
        document=Clientdocument(client=Clientdata(obj.id))
        global filename
        filename="doc%s.pdf"%(obj.id)
        document.pdfdata.save(filename,File(BytesIO(pdf.content)))
        document.save()
        today_date=datetime.date.today()
        img=qrcode.make("QR code created date:%s\n\n Name:'%s'\n\n Email Address:'%s'\n\n Contact No:'%s'\n\n Gender:'%s'\n\n Address:'%s'\n\n Distrct:'%s'\n\n Contry:'%s'\n\n Pincode:'%s'\n\n Education:'%s'\n\n Adhar No:'%s'"%(str(today_date),str(name),str(email),str(phone),str(gender),str(address),str(district),str(contry),str(pincode),str(education),str(adhar)))
        imgfile="img%s.jpg"%(obj.id)
        img.save(imgfile)
        buffer=BytesIO()
        img.save(buffer,'PNG')
        document.qrdata.save(imgfile,File(buffer))
        #return render(request,"")

        #return render(request,"clientprofilecard.html",{'obj':obj,'obj1':obj1})
        return render(request,"downloaded.html",{'document':document})
def clientadminmsg(request):
    return render(request,"clientadminmsg.html")
def clientlogin(request):
    if request.method=="GET":
        print("in get method")
        return render(request,'clientlogin.html')
    else:

        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(email,pwd)
        error_message=None
        try:
            client_obj=Client.objects.get(email=email)
        except:
            error_message='Client does not exist'
            return render(request,'clientlogin.html',{'error':error_message})
        data={'client_obj':client_obj}
        print ("data=",data)
        if client_obj and client_obj.status==1:
            if(pwd==client_obj.pwd):
                flag=1
            if flag:
                request.session['id']=client_obj.id
                request.session['name']=client_obj.clientname
                return render(request,'clienthome.html',data)
            else:
                error_message='email or password invalid'
                return render(request,'clientlogin.html',{'error':error_messege})
        else:
            if client_obj.status==0:
                error_message='admin permition required'
            else:
                error_message='email or password invalid'
        return render(request,'clientlogin.html',{'error':error_messege})                
        
    return render(request,'clientlogin.html')  
def downloaded(request):
    return render(request,"downloaded.html")
def logoutclient(request):
    request.session.clear()
    return redirect('/')
def adminhome(request):
    return render(request,'adminhome.html')   