# Generated by Django 4.1.7 on 2023-03-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0002_alter_registration_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='address_line_1',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='address_line_2',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobile_number',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='pin_code',
            field=models.CharField(default='null', max_length=6),
        ),
        migrations.AlterField(
            model_name='registration',
            name='state',
            field=models.CharField(default='null', max_length=40),
        ),
    ]
