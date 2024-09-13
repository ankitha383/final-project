from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'mov_list.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('mov_list')  # Make sure this name matches your URL pattern
    else:
        form = MovieForm()
    
    return render(request, 'add_mov.html', {'form': form })

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('mov_list')
    
    return render(request, 'delete_mov.html', {'movie': movie})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('mov_list')
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'update_mov.html', {'form': form, 'movie':movie})