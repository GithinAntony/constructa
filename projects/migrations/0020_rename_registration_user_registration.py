# Generated by Django 4.1.7 on 2023-03-26 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_registration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='user_registration',
        ),
    ]
