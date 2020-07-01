from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello world')


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
        return {'Nada encontrado'}


def fname(request, name):
    return HttpResponse(lerDoBanco(name))
