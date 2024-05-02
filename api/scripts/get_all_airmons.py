import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airmon.settings')
django.setup()

from api.models.airmon import Airmon

# Get all possible airmons
airmons = Airmon.objects.all()

# Print all information about each airmon
for airmon in airmons:
    print(f'{airmon.name} - {airmon.rarity}')

print(len(airmons))
