from django.shortcuts import render
from django.forms import ModelForm
from movies.models import Movies
from django.views.generic import DetailView
# Create your views here.

def index(request):
    objets=Movies.objects.all().order_by('rate')
    return render(request,'movies/index.html',{'movies':objets})

class MoviesDetailView(DetailView):
    model = Movies
    context_object_name = 'movie'