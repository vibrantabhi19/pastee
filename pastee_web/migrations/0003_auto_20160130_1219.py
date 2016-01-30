# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastee_web', '0002_remove_paste_paste_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('identifier', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='paste',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pastee_web.Language'),
            preserve_default=False,
        ),
    ]