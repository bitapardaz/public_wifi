# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('confirmed', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(max_length=300, null=True, upload_to=b'images')),
                ('date_published', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('confirmed', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('file_path', models.FilePathField(path=b'/mnt/FlashDrive/wifi_storage/movies/', null=True, blank=True)),
                ('category', models.ForeignKey(to='content.Category')),
            ],
        ),
    ]
