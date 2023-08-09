# Generated by Django 4.1.7 on 2023-03-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_alter_projects_end_date_alter_projects_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_status',
            field=models.CharField(choices=[('started', 'Pending'), ('ongoing', 'Active'), ('completed', 'Completed')], default='started', max_length=15),
        ),
        migrations.AddField(
            model_name='projects',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
