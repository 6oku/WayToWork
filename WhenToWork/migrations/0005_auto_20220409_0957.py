# Generated by Django 3.2.9 on 2022-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhenToWork', '0004_auto_20220407_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='New Note', max_length=255),
        ),
        migrations.AlterField(
            model_name='list',
            name='item',
            field=models.CharField(max_length=200, null=True),
        ),
    ]