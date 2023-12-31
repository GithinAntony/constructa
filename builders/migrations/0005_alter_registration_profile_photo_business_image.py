# Generated by Django 4.1.7 on 2023-03-16 13:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0004_registration_business_address_line_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='builders/'),
        ),
        migrations.CreateModel(
            name='business_image',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='builders/business/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_image_conn', to='builders.registration')),
            ],
        ),
    ]
