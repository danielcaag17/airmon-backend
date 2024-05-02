from api.scripts.django_setup import setup_django

setup_django()

from api.models.spawn_point import SpawnPoint

# Get all possible spawn_points
spawn_points = SpawnPoint.objects.all()

# Print all information about each spawn_point
for spawn_point in spawn_points:
    print(str(spawn_point))

print(len(spawn_points))
