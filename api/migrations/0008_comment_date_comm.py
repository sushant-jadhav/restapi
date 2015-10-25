# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_comm',
            field=models.DateTimeField(null=True),
        ),
    ]
