from rest_framework import serializers
from .models import *

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):

    # director = serializers.SerializerMethodField()
    # genre = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields=('director','name','popularity','imdb_score','genre')
        depth = 1
        read_only=('director','genre')


