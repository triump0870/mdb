from movie.models import Movie, Genre
from api.permissions import IsOwnerOrReadOnly
from api.serializers import MovieSerializer, UserSerializer

import django_filters

from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import filters
# from rest_framework import mixins
# Create your views here.
User = get_user_model()

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['name', 'director']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail`actions
    for the User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`
    `update` and `destroy` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,
                                    IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MovieFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre',None)
        if genre is not None:
            q = []
            for i in genre.split(','):
                q.append(Genre.objects.filter(genre__contains=i))
            for i in q:
                queryset = queryset.filter(genre=i)
        return queryset

