from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse
from . import models, forms
from .models import Movies, Vapes, Dorama


def all_vapes(request):
    vapes = Vapes.objects.all()
    return render(request, "parsed-vapes.html", {"vapes": vapes})


def all_movies(request):
    movies = Movies.objects.all()
    return render(request, "parsed-movies.html", {"movies": movies})


def all_doramas(request):
    doramas = Dorama.objects.all()
    return render(request, "parsed-dorama.html", {"doramas": doramas})


class ParserFormView(generic.FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponse("Parsed data successfully")
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
