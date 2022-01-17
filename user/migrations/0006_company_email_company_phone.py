# Generated by Django 4.0.1 on 2022-01-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_company_email_remove_company_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
    ]
