from rest_framework import serializers
from movie.models import Movie, Genre
import six
import re
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

    # def validate(self, data):
    #     """
    #     Validates the incoming data.
    #     """
    #     name = data['name']
    #     director = data['director']
    #     if not re.match(r'[A-Za-z]',name):
    #         raise serializers.ValidationError("")
    def validate_owner(self, value):
        """
        Check if the user is a valid user or not.
        """
        if not value.is_authenticated():
            raise serializers.ValidationError("User need to be a valid user to create Movie Instance")
        return value

    def validate_name(self, value):
        """
        Check that the director contains only valid string characters.
        """
        if not re.match('[A-Za-z]',value):
            raise serializers.ValidationError("Name should be valid string characters")
        return value

    def validate_director(self, value):
        """
        Check that the director contains only valid string characters.
        """
        if not re.match('[A-Za-z]',value):
            raise serializers.ValidationError("Name should be valid string characters")
        return value


