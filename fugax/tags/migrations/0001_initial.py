# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('parent_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tags.Tag')),
            ],
        ),
    ]
