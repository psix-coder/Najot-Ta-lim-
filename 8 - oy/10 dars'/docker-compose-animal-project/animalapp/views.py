from django.shortcuts import render, get_object_or_404

from .models import Category, Animal


def home_view(request):
    categories = Category.objects.all()
    animals = Animal.objects.all()

    context = {
        "categories": categories,
        "animals": animals
    }
    return render(request, 'index.html', context)


def animals_by_category(request, category_id):
    categories = Category.objects.all()
    animals = Animal.objects.filter(category_id=category_id)

    context = {
        "categories": categories,
        "animals": animals
    }
    return render(request, 'index.html', context)


def detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal
    }
    return render(request, 'detail.html', context)
