# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0003_meeting_meeting_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date_chosen',
            field=models.DateTimeField(null=True, verbose_name=b'Date_Selected', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(blank=True, to='doodle.Room', null=True),
            preserve_default=True,
        ),
    ]
