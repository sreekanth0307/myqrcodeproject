from django.db import models

class Client(models.Model):
    clientname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=30)
    contactno=models.CharField(max_length=15)
    adhar=models.CharField(max_length=12,default='000000000000')
    photo=models.ImageField(upload_to="client_data")
    status=models.BooleanField(default=False)
class Clientdata(models.Model):
    #dob=models.DateField(null=True,blank=True,default=None)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=20)
    contry=models.CharField(max_length=30)
    pincode=models.CharField(max_length=8)
    education=models.CharField(max_length=30)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
class Clientdocument(models.Model):
    pdfdata=models.FileField(upload_to='documents',null=True,blank=True)
    qrdata=models.ImageField(upload_to='qrcode',null=True,blank=True)
    client=models.ForeignKey(Clientdata,on_delete=models.CASCADE) 

        


# Create your models here.
