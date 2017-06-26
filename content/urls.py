"""public_wifi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^homepage/',views.homepage),
    url(r'^get_movies_per_category/(?P<cat_id>[0-9]+)/(?P<page>[0-9]+)/',views.get_movies_per_category),
    url(r'^get_movie_details/(?P<movie_id>[0-9]+)/',views.get_movie_details),
    url(r'^check_voucher/(?P<voucher_id>[0-9]+)/',views.check_voucher),
]
