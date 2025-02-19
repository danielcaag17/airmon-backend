import geohash
import random
from collections import defaultdict

from api.models.measure import Measure
from api.models.spawned_airmon import SpawnedAirmon
from api.models.spawn_point import SpawnPoint
from api.models.airmon import Airmon
from api.models.rarity_type import RarityType
from api.models.event import Event

PROBABILITIES = {
    RarityType.COMMON: 0.4,
    RarityType.SPECIAL: 0.3,
    RarityType.EPIC: 0.22,
    RarityType.MYTHICAL: 0.07,
    RarityType.LEGENDARY: 0.01,
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
    events = Event.objects.all()
    event_geohashes = {event.geohash.geohash[:7] for event in events}
    event_neighbors = set()
    for event_geohash in event_geohashes:
        event_neighbors.update(geohash.neighbors(event_geohash))
    event_geohashes.update(event_neighbors)

    spawned_airmons = []
    for spawn_point in spawn_points:

        # Check if the event is close
        if spawn_point.location.geohash in event_geohashes:
            event_close = True
        else:
            event_close = False

        # Airmon x hour in the day
        for hour in range(24):
            prob = random.randint(0, 100)
            if prob < 41:
                apparition_by_icqa = random.randint(-1, 6)

                # More airmons if event close
                if event_close:
                    apparition_by_icqa += 2
                current_icqa = measure_dict.get(spawn_point.station.code).icqa \
                    if measure_dict.get(spawn_point.station.code) else 1
                if apparition_by_icqa >= current_icqa:
                    # Generate the rarity
                    random_rarity = random.choices(rarities, weights=weights, k=1)[0]

                    # Get the airmon
                    random_airmon = random.choices(airmons_by_rarity[random_rarity])[0]

                    # Move from the spawn point
                    variable_longitude = random.uniform(-0.001, 0.001)
                    variable_latitude = random.uniform(-0.001, 0.001)

                    spawned_airmons.append(
                        SpawnedAirmon(
                            spawn_point=spawn_point,
                            airmon=random_airmon,
                            hour=hour,
                            variable_latitude=variable_latitude,
                            variable_longitude=variable_longitude
                        )
                    )
    SpawnedAirmon.objects.bulk_create(spawned_airmons)
