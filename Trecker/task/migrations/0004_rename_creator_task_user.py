# Generated by Django 5.0.4 on 2024-06-01 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_comment_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='creator',
            new_name='user',
        ),
    ]
