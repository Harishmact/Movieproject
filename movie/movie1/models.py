from django.db import models

# Create your models here.
class mnames(models.Model):
    name=models.CharField(max_length=20)
    dec=models.CharField(max_length=50)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movie1/image,null=True,blank=True")