# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151016_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
