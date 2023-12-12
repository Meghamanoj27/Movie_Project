from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.models import Movies

from .forms import MovieForms


# Create your views here.
def index(request):
    movie_obj = Movies.objects.all()
    context = {
        'movies': movie_obj,
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie_obj = Movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie_obj})


# def demo(request):
#     movie_obj = Movies.objects.all()
#     context = {
#         'movies': movie_obj,
#     }
#     return render(request, 'demo.html',context)


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie_var = Movies(name=name, desc=desc, year=year, img=img)
        movie_var.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie_variable = Movies.objects.get(id=id)
    formvar = MovieForms(request.POST or None, request.FILES, instance=movie_variable)
    if formvar.is_valid():
        formvar.save()
        return redirect('/')
    return render(request, 'edit.html', {'formkey': formvar, 'movie': movie_variable})


def delete(request, id):
    if request.method == 'POST':
        moviev = Movies.objects.get(id=id)
        moviev.delete()
        return redirect('/')
    return render(request, 'delete.html')
