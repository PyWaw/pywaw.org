# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=9)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
                ('sponsor', models.ForeignKey(to='meetups.Sponsor', null=True, blank=True)),
                ('venue', models.ForeignKey(to='meetups.Venue', null=True, blank=True)),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
    ]
