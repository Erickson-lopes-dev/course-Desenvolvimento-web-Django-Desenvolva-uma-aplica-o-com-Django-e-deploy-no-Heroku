from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def person_new(request):
    # modo de enviar o formulário, e arquivos de media
    form = PersonForm(request.POST, None, request.FILES)

    # validando fomulário
    if form.is_valid():
        form.save()
        return redirect('person_list')
    # retorna o template e envia o form ao html
    return render(request, 'person_form.html', {'form': form})
