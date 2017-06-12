# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Movie, Category,MovieParticipant, Participant, ParticipantType

# Register your models here.

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(MovieParticipant)
admin.site.register(Participant)
admin.site.register(ParticipantType)
