# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0005_auto_20150224_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datechoice',
            name='meeting_desc',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='nbVotes',
        ),
        migrations.AddField(
            model_name='datechoice',
            name='nbVotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
