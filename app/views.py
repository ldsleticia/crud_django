from app.form import CarrosForm
from app.models import Carros
from django.shortcuts import render, redirect


def home(request):
    data = {'db': Carros.objects.all()}
    return render(request, 'index.html', data)


def form(request):
    data = {'form': CarrosForm()}
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')
