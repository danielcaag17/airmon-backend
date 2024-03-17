# Generated by Django 4.1.13 on 2024-03-16 16:18

import api.models.airmon_type
import api.models.language
import api.models.location
import api.models.rarity_type
import api.models.unit_type
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airmon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('rarity', models.CharField(choices=[(api.models.rarity_type.RarityType['LLEGENDARI'], 'Llegendari'), (api.models.rarity_type.RarityType['EPIC'], 'Epic'), (api.models.rarity_type.RarityType['CURIOS'], 'Curios'), (api.models.rarity_type.RarityType['ESPECIAL'], 'Especial'), (api.models.rarity_type.RarityType['COMU'], 'Comu')], max_length=32)),
                ('type', models.CharField(choices=[(api.models.airmon_type.AirmonType['LOREM'], 'Lorem'), (api.models.airmon_type.AirmonType['IPSUM'], 'Ipsum'), (api.models.airmon_type.AirmonType['DOLOR'], 'Dolor')], max_length=32)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('rarity', models.CharField(choices=[(api.models.rarity_type.RarityType['LLEGENDARI'], 'Llegendari'), (api.models.rarity_type.RarityType['EPIC'], 'Epic'), (api.models.rarity_type.RarityType['CURIOS'], 'Curios'), (api.models.rarity_type.RarityType['ESPECIAL'], 'Especial'), (api.models.rarity_type.RarityType['COMU'], 'Comu')], max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[api.models.location.validate_longitude])),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[api.models.location.validate_latitude])),
            ],
            options={
                'unique_together': {('latitude', 'longitude')},
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pollutant',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('measure_unit', models.CharField(choices=[(api.models.unit_type.UnitType['MICROGRAMSxMETRE3'], 'Micrograms/m3'), (api.models.unit_type.UnitType['MILIGRAMSxMETRES3'], 'Miligrams/m3')], max_length=32)),
                ('recommended_limit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('language', models.CharField(choices=[(api.models.language.Language['CATALA'], 'Catala'), (api.models.language.Language['ANGLES'], 'Angles'), (api.models.language.Language['CASTELLA'], 'Castella')], max_length=16)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.user')),
                ('xp_points', models.PositiveSmallIntegerField()),
                ('coins', models.PositiveSmallIntegerField()),
            ],
            bases=('api.user',),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='PollutantMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.measure')),
                ('pollutant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pollutant')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='measure',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.station'),
        ),
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('attemps', models.PositiveSmallIntegerField()),
                ('airmon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.airmon')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='airmon',
            constraint=models.UniqueConstraint(fields=('name', 'rarity', 'type'), name='airmon_unique'),
        ),
        migrations.AlterUniqueTogether(
            name='pollutantmeasure',
            unique_together={('pollutant_name', 'measure')},
        ),
        migrations.AlterUniqueTogether(
            name='playeritem',
            unique_together={('item_name', 'username')},
        ),
        migrations.AddField(
            model_name='player',
            name='actual_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.location'),
        ),
        migrations.AddConstraint(
            model_name='measure',
            constraint=models.UniqueConstraint(fields=('station_code', 'date', 'hour'), name='measure_unique'),
        ),
        migrations.AlterUniqueTogether(
            name='capture',
            unique_together={('username', 'airmon'), ('username', 'date')},
        ),
    ]
