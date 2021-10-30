from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Movie
from django.shortcuts import render

""" class HomeView(ListView):
    model = Movie 
    template_name = 'base.html """

def HomeView(request):
    return render(request,'base.html')


def GenreView(request):
    if request.method=='POST':
        genre_name = request.POST.get('genre',None)
    else:    
        return render(request, 'genre.html')

def imdbView(request):
    return render(request, 'imdb.html')

def plotView(request):
    return render(request, 'plot.html')
