from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello world')


def articles(request, year):
    return HttpResponse(f'Year = {year}')
