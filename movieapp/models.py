from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    popularity = models.DecimalField(max_digits=3, decimal_places=1 )
    imdb_score = models.DecimalField(max_digits=2, decimal_places=1)
    name = models.CharField(max_length=200)
    director = models.ForeignKey(Director)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


