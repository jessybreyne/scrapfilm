from django.urls import path
from .views import index,MoviesDetailView

urlpatterns=[
    path('',index,name='index'),
    path('detailsMovies/<int:pk>',MoviesDetailView.as_view(),name='details')
]