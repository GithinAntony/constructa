# Generated by Django 4.1.7 on 2023-03-23 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_rename_messages_messages_contain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages_contain',
            name='msg_index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_index_conn', to='projects.messages_index'),
        ),
    ]