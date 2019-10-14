from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from movies.models import Movies
from django.views.generic import DetailView
# Create your views here.

class AddMoviesForm(forms.Form):
    class Meta:
        model = Movies
        name= forms.CharField(initial='your Name'),
        img= forms.URLField(initial='https://'),
        rate= forms.IntegerField(),
        years= forms.DateField(),
        description= forms.CharField()


def addMovie(request):
    form = AddMoviesForm();
    return render(request,'movies/formAddMovie.html', {'addMovie_form':form})

def index(request):
    objets=Movies.objects.all().order_by('rate')
    return render(request,'movies/index.html',{'movies':objets})

class MoviesDetailView(DetailView):
    model = Movies
    context_object_name = 'movie'