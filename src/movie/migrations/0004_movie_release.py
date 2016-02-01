# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20160130_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release',
            field=models.DateField(default=datetime.datetime(2016, 2, 1, 10, 41, 48, 128515, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
