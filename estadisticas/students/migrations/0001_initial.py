# Generated by Django 4.0.8 on 2022-10-27 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=100)),
                ('current_cueanexo', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
                ('service_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
    ]
