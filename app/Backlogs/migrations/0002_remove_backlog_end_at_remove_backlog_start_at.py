# Generated by Django 4.2 on 2023-06-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backlogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backlog',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='start_at',
        ),
    ]
