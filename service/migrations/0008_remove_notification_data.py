# Generated by Django 4.0.1 on 2022-02-17 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_notification_data_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='data',
        ),
    ]
