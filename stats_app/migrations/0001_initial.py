# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='ahelium', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='rec-engine-sb', max_length=100)),
                ('description', models.CharField(default='SB Rec Engine', max_length=500)),
                ('githubuser', models.ForeignKey(to='stats_app.GithubUser')),
            ],
        ),
    ]
