# Generated by Django 2.0.2 on 2018-04-09 10:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180312_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleEvent2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
