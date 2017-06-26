# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from content.models import Movie

# Create your models here.

class HomePageBanner(models.Model): 
	image = models.ImageField(upload_to="images")
	movie = models.ForeignKey(Movie)
	order = models.IntegerField(default=0)

class RecommendedMovies(models.Model): 
	movie = models.ForeignKey(Movie)
	order = models.IntegerField(default=0)

