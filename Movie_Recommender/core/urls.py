from django.urls import path

from  .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView),
   

    path('search/',SearchView.as_view(), name="search"),
    path('genre',GenreView, name="genre"),
    path('imdb',imdbView, name="imdb"),
    path('plot',plotView, name="plot"),



    
]
