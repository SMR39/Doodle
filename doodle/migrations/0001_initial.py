# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_to_be_choosed', models.DateTimeField(verbose_name=b'Date To be Choosed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_chosen', models.DateTimeField(verbose_name=b'Date_Selected')),
                ('nbVotesRequired', models.IntegerField(default=10)),
                ('nbVotes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(to='doodle.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datechoice',
            name='meeting',
            field=models.ForeignKey(to='doodle.Meeting'),
            preserve_default=True,
        ),
    ]
