from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def Loginpage(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        datas = Userform.objects.all()
        for i in datas:
            if i.username == username and i.password == password:
                return render(request, 'loginsuccessfully.html')
            else:
                message = "username or password incorrect"
    except:
        message = ""
    
        
    return render(request,"login.html",{"message":message})
def Signuppage(request):

    try:
        username = request.POST['username']
        password = request.POST['password']
        Userform(username = username, password = password).save()
    except:
        username = ""
        password = ""
   
    return render(request,"signup.html")
    