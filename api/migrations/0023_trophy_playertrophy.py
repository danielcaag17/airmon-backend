# Generated by Django 4.2.11 on 2024-05-08 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0022_alter_friendship_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('Or', 'Or'), ('Plata', 'Plata'), ('Bronze', 'Bronze')], default='Bronze', max_length=32)),
                ('xp', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('name', 'type')},
            },
        ),
        migrations.CreateModel(
            name='PlayerTrophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('trophy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trophy')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('username', 'trophy')},
            },
        ),
    ]
