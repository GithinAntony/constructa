# Generated by Django 4.1.7 on 2023-03-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_rename_registration_user_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_profile',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_banner_photo', models.ImageField(blank=True, upload_to='builders/')),
                ('business_title', models.CharField(blank=True, max_length=255, null=True)),
                ('business_description', models.CharField(blank=True, max_length=500, null=True)),
                ('business_email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('business_mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('business_address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('business_address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('business_district', models.CharField(blank=True, max_length=100, null=True)),
                ('business_state', models.CharField(blank=True, max_length=40, null=True)),
                ('business_pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('business_solution', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_profie_conn', to='projects.user_registration')),
            ],
        ),
        migrations.RemoveField(
            model_name='messages_contain',
            name='architects_user',
        ),
        migrations.RemoveField(
            model_name='messages_contain',
            name='builders_user',
        ),
        migrations.RemoveField(
            model_name='messages_contain',
            name='civil_engineers_user',
        ),
        migrations.RemoveField(
            model_name='messages_contain',
            name='client_user',
        ),
        migrations.RemoveField(
            model_name='messages_contain',
            name='contractors_user',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='recipient_id',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='recipient_user_type',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='sender_id',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='sender_user_type',
        ),
        migrations.AddField(
            model_name='messages_contain',
            name='participant_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.user_registration'),
        ),
        migrations.AddField(
            model_name='messages_index',
            name='recipient_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='recipient_images_conn', to='projects.user_registration'),
        ),
        migrations.AddField(
            model_name='messages_index',
            name='sender_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sender_images_conn', to='projects.user_registration'),
        ),
        migrations.CreateModel(
            name='business_profile_image',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='builders/business/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('business_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_profie_image_conn', to='projects.business_profile')),
            ],
        ),
    ]