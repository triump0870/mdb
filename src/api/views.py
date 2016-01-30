from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from movie.models import Movie
from api.serializers import MovieSerializer
# Create your views here.

class MovieListView(generics.ListCreateAPIView):
    """
    List all the Movies, or create a new Movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def get(self, request):
    #     serializer =self.serializer_class(self.get_queryset(), many=True)
    #     return Response(serializer.data)
