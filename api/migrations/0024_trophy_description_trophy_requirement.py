# Generated by Django 4.2.11 on 2024-05-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_trophy_playertrophy'),
    ]

    operations = [
        migrations.AddField(
            model_name='trophy',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='trophy',
            name='requirement',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
