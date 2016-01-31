from rest_framework import serializers
from movie.models import Movie, Genre
import six
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    movies_list = serializers.PrimaryKeyRelatedField(many=True,read_only=True, source='movies')
    class Meta:
        model = User
        fields = ('id','name','email','movies_list')

class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return six.text_type(value)

    def to_internal_value(self, value):
        item = Genre.objects.get(genre=value)
        return item.pk

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreField(queryset=Genre.objects.all(),many=True,source='genre', read_only=False)
    genres = CustomPrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, source='genre')
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Movie
        fields = ('id','popularity', 'director','imdb_score','genres', 'name', 'owner')

    # def create(self, validated_data):
    #     popularity_data = validated_data['popularity']
    #     director_data =  validated_data['director']
    #     if not isinstance(popularity_data, float):
    #         raise serializers.ValidationError("Popularity field is not correct")
    #     #if director_data is not in re.:
    #      #   raise serializers.ValidationError("Director field should be of Type String")
    #     print validated_data
    #     movie = Movie.objects.create(**validated_data)
    #     return movie

