from django.contrib import admin
from movies.models import Movies,Actor,Movie_has_Actor,ScrappingLoader
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=('name','img','rate','years','description')
admin.site.register(Movies,MovieAdmin)
