# Generated by Django 2.0.2 on 2018-04-26 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_auto_20180416_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='event',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='participants',
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='participation',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='event',
            name='coordinates',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Participation',
        ),
        migrations.AddField(
            model_name='starred',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='starred',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]