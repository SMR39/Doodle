# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(default=b'Open', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date_chosen',
            field=models.DateTimeField(null=True, verbose_name=b'Date_Selected'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(to='doodle.Room', null=True),
            preserve_default=True,
        ),
    ]
