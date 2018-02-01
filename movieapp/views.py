from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for Movies
    requires Authentication header token
    query param for search :
    name , director , genre

    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        name = self.request.query_params.get('name', None)
        director = self.request.query_params.get('director', None)
        genre = self.request.query_params.get('genre', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if director is not None:
            queryset = queryset.filter(director_name=director)
        if genre is not None:
            queryset = queryset.filter(genere__name=genre)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DirectorViewSet(viewsets.ModelViewSet,):
    """
    A viewset that provides the standard actions
    for Directors
    requires Authentication header token
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class GenreViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for Genre
    requires Authentication header token
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MoviePublicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides only list and retrieve actions
    for movies
    public api, does not require Authentication token
    query param for search :
    name , director , genre
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        name =  self.request.query_params.get('name',None)
        director = self.request.query_params.get('director', None)
        genre = self.request.query_params.get('genre', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if director is not None:
            queryset = queryset.filter(director_name=director)
        if genre is not None:
            queryset = queryset.filter(genere__name=genre)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

