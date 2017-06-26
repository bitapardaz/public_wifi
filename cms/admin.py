# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import HomePageBanner,RecommendedMovies


# Register your models here.

admin.site.register(HomePageBanner)
admin.site.register(RecommendedMovies)

