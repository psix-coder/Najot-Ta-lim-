from django.shortcuts import render, get_object_or_404
from .models import Turlar, Gullar
from .form import GullarForm

def index(request):
    turlar = Turlar.objects.all()
    gullar = Gullar.objects.all()
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'app/type.html', context)

def posts_by_turlar(request, turlar_id):
    turlar = get_object_or_404(Turlar, id=turlar_id)
    gullar = Gullar.objects.filter(type_id=turlar_id)
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'app/type.html', context)

def posts_by_gullar(request, gullar_id):
    gul = get_object_or_404(Gullar, id=gullar_id)
    context = {
        'gul': gul
    }
    return render(request, 'app/gulllar_detail.html', context)

def add_post(request, ):
    if request.method == 'POST':
        form = GullarForm(data=request.POST)
        if form.is_valid():
            lesson = Gullar.objects.create(
                **form.cleaned_data
            )
            print(lesson, "Qo'shildi!")

    form = GullarForm()
    context = {
        "form": form
    }
    return render(request, 'blok/add_post.html', context)


def update_post(request, gullar_id):
    turlar = get_object_or_404(Gullar, id=gullar_id)

    if request.method == 'POST':
        form = GullarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            turlar.name = form.cleaned_data.get('name')
            turlar.price = form.cleaned_data.get('price')
            turlar.type = form.cleaned_data.get('type')
            turlar.save()
 
    form = GullarForm(initial={
        'name':turlar.name,
        'content':turlar.price,
        'course':turlar.type
    })

    context = {
        "form":form 
    }
    return render(request, 'app/add_post.html', context)



    