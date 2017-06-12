# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieParticipant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movieparticipant',
            name='ParticipantType',
            field=models.ForeignKey(to='content.ParticipantType'),
        ),
        migrations.AddField(
            model_name='movieparticipant',
            name='movie',
            field=models.ForeignKey(to='content.Movie'),
        ),
        migrations.AddField(
            model_name='movieparticipant',
            name='participant',
            field=models.ForeignKey(to='content.Participant'),
        ),
    ]
