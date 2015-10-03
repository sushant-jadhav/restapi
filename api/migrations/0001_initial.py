# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans_text', models.CharField(max_length=b'1000', null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'1000', null=True)),
                ('about', models.CharField(max_length=b'1000', null=True)),
                ('date_create', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('date_create',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'1000', null=True)),
                ('username', models.CharField(max_length=b'1000', null=True)),
                ('password', models.CharField(max_length=b'1000')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
