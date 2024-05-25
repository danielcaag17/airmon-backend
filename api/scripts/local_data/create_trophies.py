def create_trophies():
    from api.scripts.local_data.trophies_data import get_trophies
    from api.models.trophy import Trophy

    Trophy.objects.all().delete()

    print("Creating Trophies")

    new_trophies = []
    trophies = get_trophies()
    for trophy in trophies:
        new_trophy = Trophy(
            name=trophy["name"],
            type=trophy["type"].value,
            description=trophy["description"],
            requirement=trophy["requirement"],
            xp=trophy["xp"],
        )

        new_trophies.append(new_trophy)
    Trophy.objects.bulk_create(
        new_trophies,
        update_conflicts=True,
        unique_fields=["name", "type"],
        update_fields=["name", "type", "description", "requirement", "xp"],
    )


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    create_trophies()
