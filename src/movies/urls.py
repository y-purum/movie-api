from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieInfoList.as_view()),
    path('<int:pk>/', views.MovieInfoDetail.as_view()),
    path('titles/', views.MovieList.as_view()),
    path('titles/<int:pk>/', views.MovieDetail.as_view()),
    path('directors/', views.DirectorList.as_view()),
    path('directors/<int:pk>/', views.DirectorDetail.as_view()),
    path('actors/', views.ActorList.as_view()),
    path('actors/<int:pk>/', views.ActorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)