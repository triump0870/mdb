from rest_framework import serializers
from movie.models import Movie, Genre
import six
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    movies = serializers.HyperlinkedIdentityField(view_name="api:movie-detail")
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
    genres = CustomPrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, source='genre')
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Movie
        fields = ('id','popularity', 'director','imdb_score','genres', 'name', 'owner')
