from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieDataSerializer
from .models import MovieData

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ = 'action')
    serializer_class = MovieDataSerializer

