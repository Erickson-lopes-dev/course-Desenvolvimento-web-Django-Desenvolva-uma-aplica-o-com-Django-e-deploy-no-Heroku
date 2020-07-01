from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse(f'Year = {year}')


def lerDoBanco(name):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 17},
        {'nome': 'pedro', 'idade': 48},
        {'nome': 'Joana', 'idade': 14}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == name:
            return f'{pessoa["nome"]} tem {pessoa["idade"]} anos'
    else:
        return 'Nada encontrado'


def fname(request, name):
    return HttpResponse(lerDoBanco(name))


def fname2(request, name):
    return render(request, 'pessoa.html', {'person_detail': lerDoBanco(name)})
