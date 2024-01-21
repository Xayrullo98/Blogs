from django.db import models


# Create your models here.

class Car_model(models.Model):
    nomi = models.CharField(max_length=200)

    def __str__(self):
        return self.nomi


class Drivers(models.Model):
    ism = models.CharField(max_length=200)
    familya = models.CharField(max_length=200, null=True, blank=True)
    modeli = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    mashina_rasm = models.ImageField(upload_to='media')
    hodim_rasm = models.ImageField(upload_to='media',null=True,blank=True)
    tel = models.CharField(max_length=20)
    telegram_link = models.CharField(max_length=200,null=True,blank=True)



