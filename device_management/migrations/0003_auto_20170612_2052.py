# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0002_auto_20170612_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_location',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='device',
            name='last_ping',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
