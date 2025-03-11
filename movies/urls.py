from django.urls import path
from . import views

urlpatterns = [
    path('api/movie/<str:movie_id>/', views.get_movie, name='get_movie'),
    path('api/movie/', views.create_movie, name='create_movie'),
]