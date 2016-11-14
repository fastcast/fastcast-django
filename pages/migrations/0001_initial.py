# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, null=True)),
                ('button', models.CharField(blank=True, max_length=70, null=True)),
                ('url', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='')),
                ('slide', models.IntegerField(default=0)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pages.Carousel')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField(help_text='Content can be written in Markdown.')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('button', models.CharField(blank=True, max_length=70, null=True)),
                ('url', models.CharField(blank=True, max_length=70, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_piece', to='pages.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections_piece', to='pages.Section'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_carousel', to='pages.Page'),
        ),
    ]