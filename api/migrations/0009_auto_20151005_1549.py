# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_like', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(related_name='QuestionUser', to='api.User', null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='ans_id',
            field=models.ForeignKey(related_name='answer', to='api.Answer', null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(related_name='Answeruser', to='api.User', null=True),
        ),
    ]
