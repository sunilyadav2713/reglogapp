from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg,con
#Register class
class index(View):
    def get(self,request):
        return render(request,'home.html')
class RegisterInput(View):
    def get(self,request):
        return render(request,'register.html')
class Register(View):
    def post(self,request):
        r1=Reg(
            fname=request.POST["firstname"],
            lname=request.POST['lastname'],
            uname=request.POST['username'],
            passw=request.POST['password'],
            cpassw=request.POST['confirm_password'],
            email=request.POST['email'],
            contact=request.POST['contact'],
            dob=request.POST['dob']
        )
        r1.save()
        return HttpResponse('your registerd succesfully')



#login classs
class Login(View):
    def get(self,request):
        return render(request,'login.html')
class Log(View):
    def post(self,request):
        qs=Reg.objects.filter(
            uname=request.POST['username'],
            passw=request.POST['password']
        )
        if qs:
            return HttpResponse('success')
        else:
            return HttpResponse('fialed')

#contact class
class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
class cont(View):
    def post(self,request):
        r2=con(
            name1=request.POST['name'],
            email=request.POST['email'],
            msg=request.POST['message']

        )
        r2.save()
        qs=con.objects.all()
        for i in qs:
            print(i.name1)
        return HttpResponse('your details submited')











# Create your views here.
