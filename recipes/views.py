from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {
        'name': 'Richardy Gabriel'
    })


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
