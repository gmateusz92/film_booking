from django import forms
from django.forms import ModelForm
from .models import MovieMaster
from . import models

#tworzymy klase
class AddMovieForm(ModelForm):
    class Meta:
        model = MovieMaster
        fields = ('m_name', 'm_desc',) # 'm_image')

class SetMovieForm(forms.ModelForm):
    class Meta:
        model = models.SetMovie
        fields = ('active', 'start_time', 'end_time', 'show', 'price')
        movie_choice = models.MovieMaster.objects.filter(setmovie__isnull=True)

        widgets = {
            'active': forms.Select(choices=movie_choice, attrs={'class': 'form-control', 'style': 'width:300px'}),
            'show': forms.Select(choices=(("1", "Morning"), ("2", "AfterNoon"), ("3", "Evening"), ("4", "Night")),
                                 attrs={'class': 'form-control', 'style': 'width:300px'}),
            'start_time': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'style': 'width:140px;'}),
            'end_time': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker1', 'style': 'width:140px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:140px;'})
        }