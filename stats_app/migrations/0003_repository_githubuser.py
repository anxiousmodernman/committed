# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0002_commit_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='githubuser',
            field=models.ForeignKey(default='', to='stats_app.GithubUser'),
            preserve_default=False,
        ),
    ]
