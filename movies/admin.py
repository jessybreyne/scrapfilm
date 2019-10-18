from django.contrib import admin
from movies.models import Movies,Actor,Movie_has_Actor,ScrappingLoader
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=('name','img','rate','years','description')
class ActorAdmin(admin.ModelAdmin):
    list_display=('first_name','surname','img')
class MovieHasActorAdmin(admin.ModelAdmin):
    list_display=('movie','acteur')
class Scrap(admin.ModelAdmin):
    change_form_template = "admin/Scrap.html"

    def response_change(self, request, obj):
        if "scrap" in request.POST:
            ScrappingLoader().toDb(request.POST['page'])
            self.message_user(request, "Le scrapping s'est bien réalisé.")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


admin.site.register(Movies,MovieAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Movie_has_Actor,MovieHasActorAdmin)
