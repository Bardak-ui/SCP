# Generated by Django 5.1.4 on 2025-01-19 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0002_alter_project_complexity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complexity',
            field=models.ForeignKey(choices=[('Низкий', 'Низкий'), ('Cредний', 'Cредний'), ('Высокий', 'Высокий'), ('Не указан', 'Не указан')], default='Не указан', on_delete=django.db.models.deletion.CASCADE, related_name='p_complexity', to='scp.status', verbose_name='Сложность'),
        ),
    ]
