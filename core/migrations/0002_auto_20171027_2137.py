# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Feature')),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SystemVersion')),
                ('value', models.ManyToManyField(null=True, to='core.FeatureOption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='systemversionmetadata',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SystemVersion'),
        ),
    ]
