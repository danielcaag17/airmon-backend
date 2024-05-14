from api.scripts.django_setup import setup_django

setup_django()

from api.models.spawned_airmon import SpawnedAirmon

# Get all possible spawn_points
spawned_airmons = SpawnedAirmon.objects.all()

# Print all information about each spawn_point
for spawned_airmon in spawned_airmons:
    print(f'{spawned_airmon.airmon.name}\n\tRarity: {spawned_airmon.airmon.rarity}\n\tSpawn point: {spawned_airmon.spawn_point.location.geohash}\n\tHour: {spawned_airmon.hour}')

print(len(spawned_airmons))
