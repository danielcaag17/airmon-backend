# Generated by Django 4.2.11 on 2024-05-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_friendship_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
