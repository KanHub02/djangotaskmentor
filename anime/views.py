from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from . import models, forms
from .models import Anime


def hello(request):
    return HttpResponse("<h1>Anime</h1>")


def all_anime(request):
    animes = Anime.objects.all()
    return render(request, "anime.html", {"animes": animes})


# Create your views here.
