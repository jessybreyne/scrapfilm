from django.contrib import admin
from movies.models import Movies,Actor,Movie_has_Actor,Commentaire
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=('name','img','rate','years','description')
class ActorAdmin(admin.ModelAdmin):
    list_display=('first_name','surname','img')
class MovieHasActorAdmin(admin.ModelAdmin):
    list_display=('movie','acteur')
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('username','commentaire','movie_id')

admin.site.index_template = "admin/Scrap.html" #Changement du template pour avoir le scrapping

admin.site.register(Movies,MovieAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Movie_has_Actor,MovieHasActorAdmin)
admin.site.register(Commentaire,CommentaireAdmin)

