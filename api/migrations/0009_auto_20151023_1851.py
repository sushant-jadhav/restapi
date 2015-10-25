# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_comment_date_comm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_text',
            field=models.CharField(max_length=b'1000000', null=True),
        ),
    ]
