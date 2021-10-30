from django.urls import path

from  .views import HomeView, GenreView ,imdbView, plotView

app_name = 'core'

urlpatterns = [
    path('', HomeView),
    path('genre',GenreView, name="genre"),
    path('imdb',imdbView, name="imdb"),
    path('plot',plotView, name="plot"),



    
]
