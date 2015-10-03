# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=1000, null=True)),
                ('first_name', models.CharField(max_length=1000, null=True)),
                ('last_name', models.CharField(max_length=1000, null=True)),
                ('email', models.CharField(max_length=1000, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
