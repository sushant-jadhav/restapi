# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151016_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comment_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='ans_id',
            field=models.ForeignKey(related_name='answer', to='api.Answer', null=True),
        ),
    ]
