# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0006_auto_20150224_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='meeting_desc',
            new_name='meeting_name',
        ),
    ]
