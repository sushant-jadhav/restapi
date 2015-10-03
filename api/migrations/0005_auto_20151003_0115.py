# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans_text', models.CharField(max_length=b'1000', null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(related_name='user', to='api.User', null=True),
            preserve_default=True,
        ),
    ]
