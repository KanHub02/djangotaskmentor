from django.urls import path
from . import views


app_name = "anime_urls"

urlpatterns = [
    path("anime/", views.hello),
    path("top-anime", views.all_anime),
]
