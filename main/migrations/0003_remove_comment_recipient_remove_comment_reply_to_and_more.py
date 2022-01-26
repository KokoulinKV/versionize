# Generated by Django 4.0.1 on 2022-01-26 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_adjustment_options_alter_comment_document_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='code',
            field=models.CharField(choices=[('1', 'Введение усовершенствований'), ('2', 'Изменение стандартов и норм'), ('3', 'Дополнительные требования заказчика'), ('4', 'Устранение ошибок'), ('5', 'Другие причины')], max_length=1, verbose_name='Шифр'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.document', verbose_name='Документ'),
        ),
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
