# Generated by Django 5.1.4 on 2025-02-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0008_profile_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='code',
        ),
        migrations.AddField(
            model_name='task',
            name='code',
            field=models.TextField(blank=True, null=True, verbose_name='Код'),
        ),
    ]
