# Generated by Django 4.1.7 on 2023-03-11 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_registration_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='profile_photo',
            new_name='profile_photo1',
        ),
    ]
