from django.urls import path
from .views import index,MoviesDetailView,response_change

urlpatterns=[
    path('',index,name='index'),
    path('detailsMovies/<int:pk>',MoviesDetailView.as_view(),name='details'),
    path('admin/scrap',response_change,name="admin")
]