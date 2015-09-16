# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('message', models.CharField(null=True, max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='repository',
            name='githubuser',
            field=models.ForeignKey(related_name='repos', to='stats_app.GithubUser'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repository',
            field=models.ForeignKey(related_name='commits', to='stats_app.Repository'),
        ),
    ]
