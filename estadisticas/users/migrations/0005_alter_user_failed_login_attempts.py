# Generated by Django 4.0.8 on 2023-02-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers_user_failed_login_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='failed_login_attempts',
            field=models.IntegerField(default=0),
        ),
    ]
