# Generated by Django 4.2 on 2023-06-14 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sprints', '0003_remove_sprint_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sprint',
            options={'ordering': ('end_at',), 'verbose_name': 'Sprint', 'verbose_name_plural': 'Sprints'},
        ),
    ]