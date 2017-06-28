from rest_framework import serializers

from models import HomePageBanner, RecommendedMovies
from content.serializers import MovieSerializer

class HomePageBannerSerializer(serializers.ModelSerializer):

	class Meta:
		model=HomePageBanner
		fields = '__all__'


class RecommendedMoviesSerializer(serializers.ModelSerializer):

	movie = serializers.SerializerMethodField('movie_details')

	def movie_details(self,recommended_movie):
	
		movie = recommended_movie.movie		
		serializer = MovieSerializer(movie)
		return serializer.data

	class Meta:
		model=RecommendedMovies
		fields = '__all__'

