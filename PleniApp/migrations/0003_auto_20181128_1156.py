# Generated by Django 2.1 on 2018-11-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PleniApp', '0002_thread_videourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='videourl',
            field=models.CharField(default='empty', max_length=200),
        ),
    ]