from rest_framework import generics
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.views import status

from django.http import Http404

from .models import MovieInfo
from .models import Movie
from .models import Genre
from .models import Director
from .models import Actor
from movies.api.serializers import MovieInfoSerializer
from movies.api.serializers import MovieSerializer
from movies.api.serializers import GenreSerializer
from movies.api.serializers import DirectorSerializer
from movies.api.serializers import ActorSerializer


class MovieInfoList(APIView):
    def get(self, request):
        serializer = MovieInfoSerializer(MovieInfo.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieInfoDetail(APIView):
    def get_object(self, pk):
        try:
            return MovieInfo.objects.get(pk=pk)
        except MovieInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MovieInfoSerializer(movies)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MovieInfoSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format=None):
        movies = self.get_object(pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieList(APIView):
    def get(self, request):
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        title = request.data.get('title', '')

        if title == '':
            return Response('Empty failed', status=status.HTTP_409_CONFLICT)

        if Movie.objects.filter(title=title):
            return Response('Duplicate failed', status=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            serializer.save()
            return Response('Content creation success', status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST) 


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorList(APIView):
    def get(self, request):
        serializer = DirectorSerializer(Director.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        name = request.data.get('name', '')

        if name == '':
            return Response('Empty failed', status=status.HTTP_409_CONFLICT)

        if Director.objects.filter(name=name):
            return Response('Duplicate failed', status=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            serializer.save()
            return Response('Content creation success', status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST)


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorList(APIView):
    def get(self, request):
        serializer = ActorSerializer(Actor.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        name = request.data.get('name', '')

        if name == '':
            return Response('Empty failed', status=status.HTTP_409_CONFLICT)

        if Actor.objects.filter(name=name):
            return Response('Duplicate failed', status=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            serializer.save()
            return Response('Content creation success', status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer