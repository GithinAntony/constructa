# Generated by Django 4.1.7 on 2023-03-13 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='usertype',
            new_name='user_type',
        ),
    ]
