from django.db import models


class Dorama(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class Vapes(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class Movies(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


# Create your models here.
