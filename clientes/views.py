from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def person_new(request):
    # modo de enviar o formulário, e arquivos de media
    form = PersonForm(request.POST or None, request.FILES or None)

    # validando fomulário
    if form.is_valid():
        form.save()
        return redirect('person_list')
    # retorna o template e envia o form ao html
    return render(request, 'person_form.html', {'form': form})


def person_update(request, id_person):
    person = get_object_or_404(Person, pk=id_person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def person_delete(request, id_person):
    person = get_object_or_404(Person, pk=id_person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})
