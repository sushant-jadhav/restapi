# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151016_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ans_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='comment_id',
            field=models.ForeignKey(related_name='comment', to='api.Comment', null=True),
        ),
    ]
