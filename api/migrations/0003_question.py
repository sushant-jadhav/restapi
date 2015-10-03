# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151003_0014'),
    ]

    operations = [
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
    ]
