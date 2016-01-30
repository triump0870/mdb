from rest_framework import serializers
from movie.models import Movie, Genre
import six

class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return six.text_type(value)

    def to_internal_value(self, value):
        item = Genre.objects.get(genre=value)
        return item.pk

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreField(queryset=Genre.objects.all(),many=True,source='genre', read_only=False)
    genres = CustomPrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, source='genre')
    class Meta:
        model = Movie
        fields = ('popularity', 'director','imdb_score','genres', 'name')

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

