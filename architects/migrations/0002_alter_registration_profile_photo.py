# Generated by Django 4.1.7 on 2023-03-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients/'),
        ),
    ]
