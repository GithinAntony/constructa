# Generated by Django 4.1.7 on 2023-03-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_alter_projects_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]