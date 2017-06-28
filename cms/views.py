# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from content.serializers import MovieSerializer,CategorySerializer,CategoryDetailedSerializer
from content.models import Movie,Category
from .models import HomePageBanner,RecommendedMovies
from .serializers import HomePageBannerSerializer,RecommendedMoviesSerializer

# Create your views here.
@api_view(['GET'])
def homepage(request):


	output = {}


	banners = HomePageBanner.objects.filter(confirmed=True)
	serializer = HomePageBannerSerializer(banners, many=True)
	output['banners'] = serializer.data

	recommended_movies = RecommendedMovies.objects.all()
	serializer = RecommendedMoviesSerializer(recommended_movies,many=True)
	output['recommended_movies'] = serializer.data


	categories = Category.objects.filter(confirmed=True)
	serializer = CategoryDetailedSerializer(categories,many=True)
	output['catogories'] = serializer.data


	return Response(output)

