# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0007_auto_20150224_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='date_chosen',
            new_name='date',
        ),
    ]
