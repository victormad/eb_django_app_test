# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trialmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, default='')),
                ('data', django_pgjson.fields.JsonBField()),
            ],
            options={
                'verbose_name': 'Greeting',
                'verbose_name_plural': 'Greetings',
            },
        ),
    ]
