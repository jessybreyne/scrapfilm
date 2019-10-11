from django.urls import path
from .views import index

urlpatterns=[
    path('',index,name='index'),
    path('add/',addMovie,name='addMovie'),
    path('detailsMovies/<int:pk>',detailsMovies,name='details')
]