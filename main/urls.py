from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name='mov_list'),
    path('add/', views.add_movie, name='add_mov'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_mov'),  
    path('update/<int:pk>/', views.update_movie, name='update_mov')  
]
