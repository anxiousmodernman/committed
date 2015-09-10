# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='message',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
