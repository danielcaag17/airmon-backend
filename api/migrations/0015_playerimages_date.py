# Generated by Django 4.2.11 on 2024-04-30 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_chat_friendship_chatmessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerimages',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
