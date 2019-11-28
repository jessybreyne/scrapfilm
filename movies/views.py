from django.shortcuts import render
from django.forms import ModelForm
from movies.models import Movies,ScrappingLoader,Actor,Movie_has_Actor,Commentaire
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.admin.models import LogEntry 
from django.db.models import Max
# Create your views here.

def index(request):
    objets=Movies.objects.all().order_by('-rate')
    return render(request,'movies/index.html',{'movies':objets})

def search(request): 
    if request.method == "POST":
        newPost = request.POST
        # Deux querySets afin d'afficher les films et les acteurs
        resultatMovie = Movies.objects.filter(name__contains=request.POST['search']) # Doit contenir le mot clef
        resultatActor = Actor.objects.filter(first_name__contains=request.POST['search']) # Doit contenir le mot clef
        return render(request,'movies/search.html',{'resultsMovie':resultatMovie,'resultsActor':resultatActor})
    else:
        message.error(request, "Une erreur est survenue lors de la recherche")
        return redirect("./")

def actors(request):
    objets= Actor.objects.values('first_name','img').annotate(id=Max('id')).order_by('first_name') #Permet d'éviter le dédoublement d'information des acteurs via le Max(ID)
    return render(request,'movies/actors.html',{'actors':objets})

def add_commentaires(request):
    if request.method == "POST":
        newPost = request.POST
        if newPost['username']!='' and newPost['message']!='':
            messages.success(request, "Commentaire envoyé") 
            movie = Movies.objects.get(id=newPost['movie_id'])
            Commentaire.objects.create(username=newPost['username'],commentaire=newPost['message'],movie_id=movie) #Creation dans la BD du commentaire
        else:
            messages.error(request,"Il manque une information importante") #Permet d'afficher les messages d'information
    else:
        messages.error(request, "Une erreur est survenue")
    return redirect("/movie/"+newPost['movie_id'])

def rm_commentaires(request):
    if request.method == "POST":
        newPost = request.POST
        if newPost['id']:
            messages.warning(request, "Commentaire supprimé")
            Commentaire.objects.get(id=newPost['id']).delete()
        else:
            messages.error(request,"Le message n'a pas pus être supprimé (IDERROR)")
    else:
        messages.error(request, "Une erreur est survenue")
    return redirect("/movie/"+newPost['movie_id'])

def response_change(request):
    """
        Script qui lance le scrapping via depuis l'admin
        Return sur l'index de l'admin avec un message d'information
        Enregistrement dans les logs
    """
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
    context_object_name = "movie"   
    template_name = "movies/movie_details.html"

class ActorDetailView(DetailView):
    model = Actor
    context_object_name = "actor"
    template_name = "movies/actor_details.html"