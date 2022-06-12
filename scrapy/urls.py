from django.urls import path
from . import views, models

app_name = "scrapy_url"
urlpatterns = [
    path("parser", views.ParserFormView.as_view(), name="parser_view"),
    path("all-movies", views.all_movies),
    path("all-vapes", views.all_vapes),
    path("all-dorama", views.all_doramas),
]
