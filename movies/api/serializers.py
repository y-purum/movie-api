from rest_framework import serializers

from movies import models


class MovieInfoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=32)
    director = serializers.CharField(max_length=32)

    class Meta:
        model = models.MovieInfo
        fields = ('id', 'title', 'rating', 'genre', 'director', 'actor', 'release_year', 'runtime')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ('title', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('title', )


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ('name', 'gender')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ('name', 'gender')