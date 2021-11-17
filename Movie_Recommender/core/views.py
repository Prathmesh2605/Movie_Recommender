from django.template import RequestContext, loader
from PIL import Image
import requests
import io
from io import BytesIO
from numbers import Complex
from django import template
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from numpy.core.numeric import moveaxis
from django.template import Context

from .models import Movie
from django.shortcuts import render

import sys
from django.views.generic import ListView
from recom import get_movie



 
""" class HomeView(ListView):
    model = Movie 
    template_name = 'base.html """

def HomeView(request):
    return render(request,'base.html')

class SearchView(TemplateView):
    template_name = "search.html"   

    def get_context_data(self, **kwargs):

        context =  super().get_context_data(**kwargs)
        genre_name =  self.request.GET.get("genre")
               
        movie_list, movie_img = get_movie(genre_name)
        context["movie_list"] = movie_list
        # base_url = "https://image.tmdb.org/t/p/original"
        #img_list = []
        #for item in movie_img:
           # img = base_url + str(item)
           # img_list.append(img) 
        
        #img_list2 = []
        #for image in img_list:
            
            #response = requests.get(image, stream=True)
            #file_like_object = response.raw

            #file_like_object = io.BytesIO()
            #file_like_object.write(response.content)
            #file_like_object.seek(0)
            #image_li = Image.open(BytesIO(response.content))
            #image_li.show()
            #return (file_like_object, mimetype = 'image/type')

        #context["img_list2"] = img_list2
        
  # def get_image_bytesio(img_list):
       # for i in img_list:
        #    r = requests.get(i)

          #  file_like_object = io.BytesIO()
          #  file_like_object.write(r.content)
          #  file_like_object.seek(0)  # move to the beginning of file after writing

        #return HttpResponse(file_like_object, content_type
       # ='image/png')    
        return context
        

def GenreView(request):
    return render(request, 'genre.html')

def imdbView(request):
    return render(request, 'imdb.html')

def plotView(request):
    return render(request, 'plot.html')
