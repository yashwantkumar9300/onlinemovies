from django.db import models

class Movietable(models.Model):
    moviename=models.CharField(max_length=50,unique=True)
    t_ype=models.CharField(max_length=30)
    rank=models.IntegerField()
    casting=models.CharField(max_length=50)
    release=models.IntegerField()
    image=models.ImageField(upload_to='image/')