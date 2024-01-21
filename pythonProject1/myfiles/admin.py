from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminCar(admin.ModelAdmin):
    list_display = ['id','nomi']

class AdminDrivers(admin.ModelAdmin):
    list_display = ['id','ism','familya','modeli','mashina_rasm','hodim_rasm','tel','telegram_link']


admin.site.register(Car_model,AdminCar)
admin.site.register(Drivers,AdminDrivers)