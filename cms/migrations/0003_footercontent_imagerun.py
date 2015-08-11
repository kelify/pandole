# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150807_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterContent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Title', models.CharField(max_length=20)),
                ('Article', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageRun',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Title', models.CharField(max_length=20)),
                ('Picture', models.ImageField(upload_to='static/file')),
                ('Url', models.URLField()),
            ],
        ),
    ]
