# Generated by Django 5.1.1 on 2024-10-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0002_chatgptcar_created_time_chatgptcar_updated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgptaccount',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatgptaccount',
            name='session_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
