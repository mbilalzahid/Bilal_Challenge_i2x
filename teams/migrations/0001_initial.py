# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:43
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teams.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(related_name='team', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_teams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='TeamInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(default=teams.models.generate_invite_code, max_length=25)),
                ('status', models.IntegerField(choices=[(0, b'PENDING'), (1, b'ACCEPTED'), (2, b'DECLINED'), (4, b'EXPIRED')], default=0)),
                ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'team invitation',
                'verbose_name_plural': 'team invitations',
            },
        ),
        migrations.AlterUniqueTogether(
            name='teaminvitation',
            unique_together=set([('email', 'code')]),
        ),
    ]
