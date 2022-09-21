from django.urls import path
from . import views

urlpatterns = [
    path('', views.addmovie, name='addmovie'),
    path('setmovie', views.setmovie, name='setmovie'),
    ]