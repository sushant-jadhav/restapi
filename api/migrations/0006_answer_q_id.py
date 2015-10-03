# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151003_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='q_id',
            field=models.ForeignKey(related_name='Question', to='api.Question', null=True),
            preserve_default=True,
        ),
    ]
