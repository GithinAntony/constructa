# Generated by Django 4.1.7 on 2023-03-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projects_image',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects_image',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]