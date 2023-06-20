# Generated by Django 4.2 on 2023-06-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0003_alter_member_role'),
        ('Tasks', '0009_alter_taskitem_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='task',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='member_tasks', to='Members.member', verbose_name='Workers'),
        ),
    ]