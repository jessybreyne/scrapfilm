from django.shortcuts import render
from django.forms import ModelForm
from movies.models import Movies,ScrappingLoader,Actor
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.admin.models import LogEntry 
# Create your views here.

def index(request):
    objets=Movies.objects.all().order_by('-rate')
    return render(request,'movies/index.html',{'movies':objets})

def search(request):
    if request.method == "POST":
        newPost = request.POST
        resultatMovie = Movies.objects.filter(name__contains=request.POST['search'])
        resultatActor = Actor.objects.filter(first_name__contains=request.POST['search'])
        return render(request,'movies/search.html',{'resultsMovie':resultatMovie,'resultsActor':resultatActor})
    else:
        message.error(request, "Une erreur est survenue lors de la recherche")
        return redirect("./")

def actors(request):
    objets=Actor.objects.all().order_by('surname')
    return render(request,'movies/actors.html',{'actors':objets})

def response_change(request):
    if request.method == "POST":
        newPost = request.POST
        if 'page' in newPost.keys():
            if int(newPost['page'])>0:
                ScrappingLoader().toDb(int(newPost['page']))
                l = LogEntry(user_id=request.user.id, action_flag=1, object_repr="Scrap terminé")
                l.save()
                messages.success(request, 'Scrap terminé, data loaded.')
                return redirect("./")
            else:
                l = LogEntry(user_id=request.user.id, action_flag=3, object_repr="nombre de page < 1")
                l.save()
                messages.error(request, 'Une erreur est survenue.')
                return redirect("./") 
        else:
            l = LogEntry(user_id=request.user.id, action_flag=3, object_repr="Erreur des paramètres")
            l.save()
            messages.error(request, 'Une erreur est survenue.')
            return redirect("./")  
    else:
        l = LogEntry(user_id=request.user.id, action_flag=3, object_repr="Erreur lors de l'appel de l'API")
        l.save()
        messages.error(request, 'Une erreur est survenue.')
        return redirect("./")

class MoviesDetailView(DetailView):
    model = Movies
    context_object_name = 'movie'
    template_name = "movies/movie_details.html"

class ActorDetailView(DetailView):
    model = Actor
    context_object_name = "actor"
    template_name = "movies/actor_details.html"