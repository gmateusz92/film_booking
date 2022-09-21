from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import AddMovieForm, SetMovieForm

def addmovie(request):
    submitted = False
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addmovie?submitted=True')
    else:
        form = AddMovieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addmovie.html', {'form': form, 'submitted':submitted})

def addmovie(request):
    submitted = False
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addmovie?submitted=True')
    else:
        form = AddMovieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addmovie.html', {'form': form, 'submitted':submitted})

def setmovie(request):
    submitted = False
    if request.method == "POST":
        form = SetMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/setmovie?submitted=True')
    else:
        form = SetMovieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'setmovie.html', {'form': form, 'submitted':submitted})