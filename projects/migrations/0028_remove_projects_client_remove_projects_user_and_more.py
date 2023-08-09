# Generated by Django 4.1.7 on 2023-03-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_remove_projects_architect_remove_projects_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='client',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.AddField(
            model_name='projects',
            name='client_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='user_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]