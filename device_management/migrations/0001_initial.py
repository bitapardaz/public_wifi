# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identification_code', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=200, null=True, blank=True)),
                ('owner_name', models.CharField(max_length=200, null=True, blank=True)),
                ('owner_mobile', models.CharField(max_length=200, null=True, blank=True)),
                ('last_location', models.CharField(max_length=200, null=True, blank=True)),
                ('last_ping', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_sent_to_driver', models.BooleanField(default=False)),
                ('is_consumed', models.BooleanField(default=False)),
                ('date_generated', models.DateTimeField(auto_now=True)),
                ('date_activated_by_consumer', models.DateTimeField()),
                ('consumer_id', models.CharField(max_length=200, null=True, blank=True)),
                ('consumer_mobile_phone', models.CharField(max_length=200, null=True, blank=True)),
                ('device', models.ForeignKey(to='device_management.Device')),
            ],
        ),
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('duration_days', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='voucher',
            name='voucher_type',
            field=models.ForeignKey(to='device_management.VoucherType'),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(to='device_management.Owner'),
        ),
    ]
