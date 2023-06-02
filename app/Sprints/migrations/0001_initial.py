# Generated by Django 4.2 on 2023-06-02 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ScrumProjects', '0007_alter_scrumproject_backlogs'),
        ('Backlogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateField(verbose_name='Start at')),
                ('end_at', models.DateField(verbose_name='End at')),
                ('backlogs', models.ManyToManyField(blank=True, related_name='backlog_sprints', to='Backlogs.backlog', verbose_name='Backlog')),
                ('scrum_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrumproject_sprints', to='ScrumProjects.scrumproject', verbose_name='Scrum project')),
            ],
            options={
                'verbose_name': 'Sprint',
                'verbose_name_plural': 'Sprints',
                'ordering': ('-end_at',),
            },
        ),
    ]
