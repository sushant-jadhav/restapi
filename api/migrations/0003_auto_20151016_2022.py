# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151009_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ans_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='comment_id',
            field=models.ForeignKey(related_name='commentid', to='api.Comment', null=True),
        ),
    ]
