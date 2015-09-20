# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0002_auto_20150916_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='githubuser',
        ),
        migrations.DeleteModel(
            name='GithubUser',
        ),
    ]
