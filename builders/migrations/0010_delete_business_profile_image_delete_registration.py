# Generated by Django 4.1.7 on 2023-03-26 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_business_profile_and_more'),
        ('builders', '0009_business_profile_image_date_updated_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='business_profile_image',
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
