# Generated by Django 4.0.1 on 2022-02-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_project_project_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(blank=True, choices=[(2, 'Линейный'), (1, 'Площадной')], null=True, verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='standardsection',
            name='project_type',
            field=models.IntegerField(blank=True, choices=[(2, 'Линейный'), (1, 'Площадной')], null=True),
        ),
    ]
