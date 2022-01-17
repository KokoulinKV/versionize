# Generated by Django 4.0.1 on 2022-01-16 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_section_expert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
