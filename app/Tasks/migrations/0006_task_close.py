# Generated by Django 4.2 on 2023-06-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0005_alter_task_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='close',
            field=models.BooleanField(default=False, verbose_name='Close'),
        ),
    ]
