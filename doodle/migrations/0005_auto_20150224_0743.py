# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0004_auto_20150213_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='datechoice',
            name='meeting_desc',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datechoice',
            name='meeting',
            field=models.ForeignKey(blank=True, to='doodle.Meeting', null=True),
            preserve_default=True,
        ),
    ]
