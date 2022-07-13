from django.shortcuts import render
from . models import *
from random import randint
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def singupPage(request):
    return render(request,"app/signup.html")


def RegisterUser(request):
        if request.POST['role']=="Candidate":
            role= request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            user = UserMaster.objects.filter(email=email)

            if user:
                message= "User already Exist"
                return render(request,"app/signup.html",{'msg':message})
            else:
                   if password == cpassword:
                       otp = randint(100000,999999)
                       newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                       newcand =Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                       return render(request,"app/otpverify.html",{'email' :email})
        else:
          print("Company Registration")


def OTPPage(request):
    return render(request,"app/otpverify.html")