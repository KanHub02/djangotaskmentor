from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    age_control = models.PositiveIntegerField()


# Create your models here.
