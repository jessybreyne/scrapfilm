from django.shortcuts import render
from django.forms import ModelForm
from myform.models import Movies
# Create your views here.

class AddMoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ('name','img','rate','years','description')
        widgets = {
            'name': text(attrs={initial:'your Name'}),
            'img': url(attrs={initial:'https://'}),
            'rate': number(attrs={max:100,min:0}),
            'years': date(),
            'description': textArea()
        }
def addMovie(request):
    form = AddMovieForm();
    returnrender(request,'formAddMovie.html', {'contact_form':form})

def index(request):
    objets=Movies.objects.all().order_by('rate')
    return render(request,'index.html',{'movies':objets})

def detailsMovies(request,nb):
    movie = Movies.objects.get(id=nb)
    return render(request,'detailsMovie.html',{'movie':movie})