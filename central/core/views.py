from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'core/index.html')

def empresas(request):
    return render(request, 'core/empresas.html')

def vagas(request):
    return render(request, 'core/vagas.html')

def servicos(request):

    return render(request, 'core/servicos.html')

def talentos(request):
    return render(request, 'core/talentos.html')

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def base(request):
    return render(request, 'core/base2.html')

