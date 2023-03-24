# Generated by Django 4.1.7 on 2023-03-23 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Projects', '0004_remove_projectcolumn_is_private_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcolumn',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_projectcolumn', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
            preserve_default=False,
        ),
    ]