# Generated by Django 4.1.7 on 2023-03-17 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0005_alter_registration_profile_photo_business_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='business_image',
            new_name='business_profile_image',
        ),
    ]