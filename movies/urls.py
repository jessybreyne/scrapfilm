from django.urls import path
from .views import index,MoviesDetailView,response_change,ActorDetailView,actors,search,add_commentaires,rm_commentaires

urlpatterns=[
    path('',index,name='index'),
    path('actors/',actors,name='actors'),
    path('actor/<int:pk>',ActorDetailView.as_view(),name='detailsActor'),
    path('movie/<int:pk>',MoviesDetailView.as_view(),name='detailsMovie'),
    path('search/',search,name='search'),
    path('add-commentaire/',add_commentaires,name="addCommentaire"),
    path('rm-commentaire/',rm_commentaires,name="rmCommentaire"),
    path('admin/scrap',response_change,name="admin")
]