# Generated by Django 4.1.7 on 2023-03-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_projects_title_image_alter_projects_architect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='usertype',
            field=models.CharField(default='null', max_length=20),
        ),
    ]