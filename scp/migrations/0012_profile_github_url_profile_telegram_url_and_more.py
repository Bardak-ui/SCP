# Generated by Django 5.1.4 on 2025-02-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0011_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='./default/no_avatar.png', null=True, upload_to='./profile_avatars/'),
        ),
    ]
