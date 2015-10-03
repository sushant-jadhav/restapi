# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_answer_q_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(related_name='User', to='api.User', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
