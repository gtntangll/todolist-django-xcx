# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(default='无', max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(default='无', max_length=128)),
                ('status', models.CharField(default='进行中', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserExt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=128, verbose_name='昵称')),
                ('headimgurl', models.CharField(max_length=128, verbose_name='头像地址')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserExt'),
        ),
    ]
