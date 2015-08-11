# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=30)),
                ('company_date_range', models.CharField(max_length=10)),
                ('company_signature', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=30)),
                ('company_logo', models.FileField(upload_to='static/file')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('style', models.CharField(choices=[('1', '风格一'), ('2', '风格二')], max_length=1)),
                ('label', models.CharField(max_length=20)),
                ('menurl', models.CharField(max_length=50)),
                ('menuweight', models.IntegerField()),
                ('styleid', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('html_content', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('createtime', models.DateTimeField()),
                ('category', models.ForeignKey(to='cms.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PageOfStyleone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PageOfStyletwo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('maximage', models.FileField(upload_to='static/file')),
            ],
        ),
        migrations.CreateModel(
            name='Styleone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Styletwo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pageofstyletwo',
            name='menu',
            field=models.ForeignKey(to='cms.Styletwo'),
        ),
        migrations.AddField(
            model_name='pageofstyleone',
            name='menu',
            field=models.ForeignKey(to='cms.Styleone'),
        ),
    ]
