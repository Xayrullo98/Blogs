from django.shortcuts import render
from myfiles.models import *

# Create your views here.

def index(request):
    cars = Car_model.objects.all()
    drivers = Drivers.objects.all()
    context = {"cars":cars,
               "drivers":drivers}
    return render(request, 'index.html',context)
