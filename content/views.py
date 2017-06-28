# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import MovieSerializer,CategorySerializer,CategoryDetailedSerializer
from models import Movie,Category
from device_management.utilities import check_user_current_voucher


@api_view(['GET'])
def check_voucher(request,voucher_id):
	print movie_id
	return Response({"status":"0","message":"error_message"})


@api_view(['GET','POST'])
def get_movie_details(request,movie_id):

	output = {}
	user_voucher = request.data.get('user_voucher')

	if check_user_current_voucher(user_voucher): 
		output['access'] = 'granted'
	else: 
		output['access'] = 'forbidden'		

	try: 

		movie = Movie.objects.get(id=movie_id)

		serializer = MovieSerializer(movie)
		output["details"] = serializer.data
		output["status"] = "0"

	except Movie.DoesNotExist: 
		output["details"] = "None"
		output["status"] = "1"
	
	return Response(output)

@api_view(['GET'])
def get_movies_per_category(request,cat_id,page):

	cat = Category.objects.get(id=cat_id)
	movies = Movie.objects.filter(category=cat,confirmed=True)

	dict={}
	serializer = MovieSerializer(movies,many=True)
	dict['movies']=serializer.data

	response = Response(dict)
	return response


