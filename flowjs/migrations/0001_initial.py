# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import flowjs.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField(max_length=255, unique=True)),
                ('original_filename', models.CharField(max_length=200)),
                ('final_file', models.FileField(blank=True, max_length=255, null=True, upload_to=flowjs.utils.chunk_upload_to)),
                ('total_size', models.IntegerField(default=0)),
                ('total_chunks', models.IntegerField(default=0)),
                ('total_chunks_uploaded', models.IntegerField(default=0)),
                ('state', models.IntegerField(choices=[(1, b'Uploading'), (2, b'Completed'), (3, b'Upload Error'), (4, b'Joining chunks'), (5, b'Joining chunks error')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowFileChunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, upload_to=flowjs.utils.chunk_upload_to)),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='flowjs.FlowFile')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
