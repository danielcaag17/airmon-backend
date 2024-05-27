def create_airmons():
    import os
    from django.core.files import File
    from django.conf import settings

    from api.scripts.local_data.airmons_data import get_airmons
    from api.models.airmon import Airmon

    # Define the path to the temp folder
    temp_folder = os.path.join(settings.BASE_DIR, "temp_airmon_pictures")
    Airmon.objects.all().delete()
    new_airmons = []
    airmons = get_airmons()
    for airmon in airmons:
        image_path = os.path.join(temp_folder, f"{airmon['name']}.png")
        new_airmon = Airmon(
            name=airmon["name"],
            description=airmon["description"],
            rarity=airmon["rarity"].value,
            type=airmon["type"].value,
        )

        with open(image_path, "rb") as image_file:
            new_airmon.image.save(
                f"{airmon['name']}.png", File(image_file), save=False
            )
        new_airmons.append(new_airmon)
    Airmon.objects.bulk_create(
        new_airmons,
        update_conflicts=True,
        unique_fields=["name"],
        update_fields=["description", "rarity", "type", "image"],
    )


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    create_airmons()
