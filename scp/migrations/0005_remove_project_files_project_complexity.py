# Generated by Django 5.1.4 on 2025-01-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0004_rename_statia_post_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='files',
        ),
        migrations.AddField(
            model_name='project',
            name='complexity',
            field=models.CharField(choices=[('Выполнено', 'Выполнено'), ('В разработке', 'В разработке'), ('Ожидает', 'Ожидает')], default='Не указан', max_length=100, verbose_name='Сложность'),
        ),
    ]