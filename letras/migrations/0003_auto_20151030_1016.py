# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0002_auto_20151030_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('banda', models.CharField(max_length=50)),
                ('integrantes', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='Fotos/')),
            ],
        ),
        migrations.AddField(
            model_name='cancione',
            name='duracion',
            field=models.CharField(max_length=15, default='00:00'),
        ),
        migrations.AddField(
            model_name='cancione',
            name='banda',
            field=models.ForeignKey(blank=True, null=True, to='letras.Banda'),
        ),
    ]
