from core.views import *
from django.urls import path, include

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
    path('base/', base),
    path('index', index, name='index'),
    path('empresas/', empresas, name='empresas'),
    path('vagas/', vagas, name='vagas'),
    path('servicos/', servicos, name='servicos'),
    path('talentos/', talentos, name='talentos'),
]
