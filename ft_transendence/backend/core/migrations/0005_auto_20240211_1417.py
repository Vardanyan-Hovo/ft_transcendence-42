# Generated by Django 3.2.24 on 2024-02-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240211_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
