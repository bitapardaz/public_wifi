# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='last_location',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='last_ping',
        ),
    ]
