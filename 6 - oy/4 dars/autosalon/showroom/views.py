from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def home(request):
    brand = Brand.objects.all()
    return render(request, 'showroom/home.html', {'brands': brand})

def car_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.filter(brand=brand)

    return render(request, 'showroom/cars.html', {'cars': car, 'brands': brand})