# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='owner',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='movies', default=1, to=settings.AUTH_USER_MODEL),
=======
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
>>>>>>> 7a05b21aec24c88adbbd8f0b4d4e967d5eb4f11f
            preserve_default=False,
        ),
    ]
