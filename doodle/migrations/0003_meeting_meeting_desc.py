# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0002_auto_20150213_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_desc',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
