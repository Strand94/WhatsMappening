# Generated by Django 2.0.2 on 2018-04-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20180426_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStarred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.ManyToManyField(related_name='favorited_by', to='events.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='starred',
            name='timestamp',
        ),
    ]
