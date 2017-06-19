# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=37)),
                ('major', models.FloatField()),
                ('minor', models.FloatField()),
                ('alias', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Campaing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('range', models.IntegerField()),
                ('card_media_url', models.CharField(max_length=1024)),
                ('card_title', models.CharField(max_length=128)),
                ('card_content', models.CharField(max_length=500)),
                ('notification_title', models.CharField(max_length=100)),
                ('notification_content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='campaing',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Store'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Store'),
        ),
    ]
