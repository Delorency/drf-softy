# Generated by Django 4.2 on 2023-06-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sprints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
