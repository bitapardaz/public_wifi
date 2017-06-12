# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import MovieSerializer,CategorySerializer,CategoryDetailedSerializer
from models import Movie,Category


@api_view(['GET'])
def check_voucher(request,voucher_id):
	print movie_id
	return Response({"status":"0","message":"error_message"})


@api_view(['GET'])
def get_movie_details(request,movie_id):
	print movie_id
	return Response({"access":"granted","link_to_play":"here"})

@api_view(['GET'])
def get_movies_per_category(request,cat_id,page):

	cat = Category.objects.get(id=cat_id)
	movies = Movie.objects.filter(category=cat,confirmed=True)

	dict={}
	serializer = MovieSerializer(movies,many=True)
	dict['movies']=serializer.data

	response = Response(dict)
	return response


@api_view(['GET'])
def homepage(request):


	dict = {}
	categories = Category.objects.filter(confirmed=True)
	serializer = CategoryDetailedSerializer(categories,many=True)
	dict['catogories'] = serializer.data

	response = Response(serializer.data)
	return response
