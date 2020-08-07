from django.db import models

class Usersignuptable(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()
    username=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)

class Userlogintable(models.Model):
    usrname=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)
