from django.shortcuts import render
from animais.models import Animal


def index(request):

    context = {'caracteristicas': None}

    if 'buscar' in request.GET:
        animais= Animal.objects.all()
        animal_pesquisado = request.GET['buscar']
        caractersticas = animais.filter(nome_animal__icontains = animal_pesquisado)
        context = {'caracteristicas' : caractersticas}
    return render(request, 'index.html', context)
