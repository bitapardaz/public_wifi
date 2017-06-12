# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0003_auto_20170612_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corrent_voucher_code_entered', models.CharField(max_length=1000)),
                ('wrong_voucher_code_entered', models.CharField(max_length=1000)),
            ],
        ),
    ]
