from movie.models import Movie, Genre
from api.permissions import IsOwnerOrReadOnly
from api.serializers import MovieSerializer, UserSerializer

import django_filters

from django.contrib.auth import get_user_model
from django.middleware import csrf
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import filters
from rest_framework import serializers
from django.core.exceptions import PermissionDenied

# from rest_framework import mixins
# Create your views here.
User = get_user_model()

class MovieFilter(django_filters.FilterSet):
    """
    It filters queryset based on the query parameter `name`, `director`, `imdb_score` and `popularity`.

    imdb_score is again divided into two query parameter, `min_imdb` and `max_imdb`

    min_imdb will return the objects which have atleast or greater imdb_score than the specified imdb_score

    max_imdb will return the objects which have atmost or less than the specified imdb_score.
    """
    min_imdb = django_filters.NumberFilter(name='imdb_score', lookup_type='gte')
    max_imdb = django_filters.NumberFilter(name='imdb_score', lookup_type='lte')
    class Meta:
        model = Movie
        fields = ['name', 'director','min_imdb','max_imdb','popularity']


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
        """
        Checks the requested user is a valid user or not.
        """
        if not self.request.user.is_authenticated():
            raise PermissionDenied
        if 'genres' not in self.request.data:
            raise serializers.ValidationError({'genres':"genres field can't be empty"})
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Filters the queryset on the query parameter `genre`
        and returns the filtered queryset.
        """
        print csrf.get_token(self.request)
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre',None)
        if genre is not None:
            q = []
            for i in genre.split(','):
                q.append(Genre.objects.filter(genre=i.title()))
            for i in q:
                queryset = queryset.filter(genre=i)
        return queryset

    def update(self, request, *args, **kwargs):
        """
        check while the updation of the instance the requesting user and the owner of
        the instance are same or not.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if not instance.owner == request.user:
            raise PermissionDenied
        self.perform_update(serializer)
        return Response(serializer.data)








