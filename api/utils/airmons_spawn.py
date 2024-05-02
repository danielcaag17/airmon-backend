import random
from collections import defaultdict

from api.models.measure import Measure
from api.models.spawned_airmon import SpawnedAirmon
from api.models.spawn_point import SpawnPoint
from api.models.airmon import Airmon

PROBABILITIES = {
    "Comu": 0.4,
    "Especial": 0.3,
    "Curios": 0.22,
    "Epic": 0.07,
    "Llegendari": 0.01,
}


def reset_spawns():
    SpawnedAirmon.objects.all().delete()


# Spawners for a whole day
def spawn_new_airmons():
    spawn_points = SpawnPoint.objects.all()

    airmons = Airmon.objects.all()
    airmons_by_rarity = defaultdict(list)
    rarities = list(PROBABILITIES.keys())
    weights = list(PROBABILITIES.values())
    for airmon in airmons:
        airmons_by_rarity[airmon.rarity].append(airmon)
    measure_dict = {measure.station_code: measure for measure in Measure.objects.all()}

    spawned_airmons = []
    for spawn_point in spawn_points:
        # Airmon x hour in the day
        for hour in range(24):
            apparition_by_icqa = random.randint(1, 6)
            current_icqa = measure_dict.get(spawn_point.station.code).icqa if measure_dict.get(spawn_point.station.code) else 1
            if apparition_by_icqa >= current_icqa:
                # Generate the rarity
                random_rarity = random.choices(rarities, weights=weights, k=1)[0]

                # Get the airmon
                random_airmon = random.choices(airmons_by_rarity[random_rarity])[0]
                spawned_airmons.append(
                    SpawnedAirmon(
                        spawn_point=spawn_point, airmon=random_airmon, hour=hour
                    )
                )
    SpawnedAirmon.objects.bulk_create(spawned_airmons)
