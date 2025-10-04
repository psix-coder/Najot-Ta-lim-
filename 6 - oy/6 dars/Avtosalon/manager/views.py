from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Brand, Car
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")


def index(request: WSGIRequest):
    brands = Brand.objects.all()
    car = Car.objects.all()
    context = {
        "brands":brands,
        "car": car
    }

    return render(request, 'brend.html', context)

def posts_by_brands(request, brand_id):
    brands = Brand.objects.get(id=brand_id)
    car = Car.objects.filter(brend_id=brand_id)
    context = {
        "brands": [brands],
        "car": car
    }
    return render(request, 'brend.html', context)

def posts_by_cars(request, car_id):
    car = Car.objects.get(id=car_id)  
    context = {
        "car": car,
    }
    return render(request, 'car.html', context)
