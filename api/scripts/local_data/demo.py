def create_demo_user():
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password
    from api.models.player import Player
    import random
    from api.models.airmon import Airmon
    from api.models.capture import Capture

    username = "demoDestroyer96"
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username="demoDestroyer96")
        user.delete()

    password = make_password('demo')
    user = User.objects.create(username=username, password=password)
    player = Player.objects.get(user=user)
    player.coins = 15000
    player.xp_points = 9000
    player.save()
    rarities = ["COMMON", "SPECIAL", "EPIC", "MYTHICAL", "LEGENDARY"]
    weights = [0.4, 0.3, 0.22, 0.07, 0.01]
    for i in range(298):
        random_index = random.choices(range(len(rarities)), weights=weights, k=1)[0]
        random_rarity = rarities[random_index]
        airmon = Airmon.objects.filter(rarity=random_rarity).order_by("?").first()
        capture = Capture.objects.create(user=user, airmon=airmon)
        if i % 10 == 0:
            capture.delete()


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    create_demo_user()
