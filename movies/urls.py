from django.urls import path
from .views import index,MoviesDetailView,response_change,ActorDetailView,actors

urlpatterns=[
    path('',index,name='index'),
    path('actors/',actors,name='actors'),
    path('actor/<int:pk>',ActorDetailView.as_view(),name='detailsActor'),
    path('movie/<int:pk>',MoviesDetailView.as_view(),name='detailsMovie'),
    path('admin/scrap',response_change,name="admin")
]