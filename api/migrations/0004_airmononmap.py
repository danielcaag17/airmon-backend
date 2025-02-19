# Generated by Django 4.1.13 on 2024-03-21 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_airmononmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirmonOnMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('expiry_date', models.BigIntegerField()),
                ('airmon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.airmon')),
            ],
            options={
                'unique_together': {('latitude', 'longitude')},
            },
        ),
    ]
