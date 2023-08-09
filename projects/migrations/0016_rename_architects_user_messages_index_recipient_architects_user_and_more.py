# Generated by Django 4.1.7 on 2023-03-23 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_remove_messages_index_recipient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages_index',
            old_name='architects_user',
            new_name='recipient_architects_user',
        ),
        migrations.RenameField(
            model_name='messages_index',
            old_name='builders_user',
            new_name='recipient_builders_user',
        ),
        migrations.RenameField(
            model_name='messages_index',
            old_name='civil_engineers_user',
            new_name='recipient_civil_engineers_user',
        ),
        migrations.RenameField(
            model_name='messages_index',
            old_name='client_user',
            new_name='recipient_client_user',
        ),
        migrations.RenameField(
            model_name='messages_index',
            old_name='contractors_user',
            new_name='recipient_contractors_user',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='sender_id',
        ),
        migrations.RemoveField(
            model_name='messages_index',
            name='sender_user_type',
        ),
    ]
