# Generated by Django 4.1.7 on 2023-03-26 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_remove_messages_index_ind_architects_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(choices=[('contractors', 'Contractors'), ('builders', 'Builders'), ('civil_engineers', 'Civil Engineers'), ('clients', 'Clients'), ('architects', 'Architects')], max_length=20)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email_address', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=500, null=True)),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='clients/')),
                ('address_line_1', models.CharField(max_length=500, null=True)),
                ('address_line_2', models.CharField(max_length=500, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('pin_code', models.CharField(max_length=8, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
