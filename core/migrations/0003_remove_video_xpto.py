# Generated by Django 5.1.2 on 2024-10-15 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_video_xpto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='xpto',
        ),
    ]
