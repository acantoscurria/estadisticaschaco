# Generated by Django 4.0.8 on 2022-11-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='to_seccion',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='to_seccion_type',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_cueanexo',
            field=models.CharField(max_length=9),
        ),
    ]
