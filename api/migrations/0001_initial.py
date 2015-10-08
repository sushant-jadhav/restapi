# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans_text', models.CharField(max_length=b'10000', null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=b'6000', null=True)),
                ('ans_id', models.ForeignKey(related_name='answer', to='api.Answer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'1000', null=True)),
                ('about', models.CharField(max_length=b'1000', null=True)),
                ('date_create', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=1000, null=True)),
                ('last_name', models.CharField(max_length=1000, null=True)),
                ('email', models.CharField(max_length=1000, null=True)),
                ('about', models.CharField(max_length=2000, null=True)),
                ('password', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(related_name='user', to='api.User', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(related_name='Answeruser', to='api.User', null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='q_id',
            field=models.ForeignKey(related_name='questionid', to='api.Question', null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(related_name='questionUser', to='api.User', null=True),
        ),
    ]
