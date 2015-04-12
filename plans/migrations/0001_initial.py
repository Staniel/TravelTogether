# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=500)),
                ('destination', models.CharField(max_length=200)),
                ('limit', models.IntegerField()),
                ('depart_time', models.DateTimeField()),
                ('return_time', models.DateTimeField()),
                ('holder', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='joinedplan',
            name='joined_plan',
            field=models.ForeignKey(to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='joinedplan',
            name='joined_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]