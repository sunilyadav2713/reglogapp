from django.db import models
class Reg(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=15)
    uname=models.CharField(max_length=15,primary_key=True)
    passw=models.CharField(max_length=10)
    cpassw=models.CharField(max_length=10)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
class con(models.Model):
    name1=models.CharField(max_length=20,primary_key=True)
    email=models.EmailField()
    msg=models.CharField(max_length=50)

