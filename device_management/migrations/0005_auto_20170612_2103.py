# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0004_config'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Config',
            new_name='Configuration',
        ),
    ]
