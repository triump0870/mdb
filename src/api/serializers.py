from rest_framework import serializers
from movie.models import Movie, Genre
import six
import re
from django.contrib.auth import get_user_model

User = get_user_model()

def match(field,value):
        if not re.match(r'[A-Za-z]', value):
            raise serializers.ValidationError({field:"%s should be valid string characters"%field})
        return value

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="api:movie-detail")
    class Meta:
        model = User
        fields = ('url','name','email','movies')

class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return six.text_type(value)

    def to_internal_value(self, value):
        item = Genre.objects.get(genre=value)
        return item.pk

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
                                        queryset=Genre.objects.all(),
                                        many=True,
                                        slug_field='genre',
                                        source='genre')

    url = serializers.HyperlinkedIdentityField(view_name='api:movie-detail')
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Movie
        fields = ('url','name', 'director','genres','release','imdb_score', 'popularity','owner')

    def validate(self, data):
        """
        Validates the data comes with the request.
        """
        name = match('name',data['name'])
        director = match('director',data['director'])
        imdb = data['imdb_score']
        popularity = data['popularity']
        if not 1<=imdb<=10:
            raise serializers.ValidationError({'imdb_score':"Invalid IMDB score"})
        if not 1<=popularity<=100:
            raise serializers.ValidationError({"popularity":"Invalid POPULARITY score"})
        return data

