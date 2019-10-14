from django.urls import path
from .views import index,addMovie,MoviesDetailView

urlpatterns=[
    path('',index,name='index'),
    path('add/',addMovie,name='addMovie'),
    path('detailsMovies/<int:pk>',MoviesDetailView.as_view(),name='details')
]