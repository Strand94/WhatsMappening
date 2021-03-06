# Generated by Django 2.0.2 on 2018-03-03 23:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('ingress', models.CharField(blank=True, default='', max_length=300)),
                ('description', models.CharField(blank=True, max_length=3000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 3, 3, 23, 22, 48, 278690, tzinfo=utc))),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, upload_to='events')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('G', 'Going'), ('I', 'Interested')], default='G', max_length=1)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Attendance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='participants',
            field=models.ManyToManyField(blank=True, through='events.Participation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('user', 'attendance')},
        ),
    ]
