from rest_framework import serializers
from models import Movie,Category

class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		model=Movie
		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model=Category
		fields = '__all__'



class CategoryDetailedSerializer(serializers.ModelSerializer):

	movies = serializers.SerializerMethodField('my_movies')

	def my_movies(self,cat):

		movies = Movie.objects.filter(category=cat,confirmed=True)
		if movies == []:
			return []

		else:
			serializer = MovieSerializer(movies,many=True)
			return serializer.data

	class Meta:
		model = Category
		fields = ('id','name','movies','thumbnail','date_published',)
