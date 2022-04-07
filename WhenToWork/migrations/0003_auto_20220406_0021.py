# Generated by Django 3.2.9 on 2022-04-05 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WhenToWork', '0002_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='time',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]