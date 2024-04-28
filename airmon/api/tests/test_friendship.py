from datetime import datetime

from django.test import TestCase

from .utils import *
from ..models import Friendship


class FriendshipModelTest(TestCase):
    def setUp(self):
        self.friend = Friendship.objects.create(
            user1=create_user("user1"),
            user2=create_user("user2"),
            date=datetime.now(get_timezone())
        )

    def test_friendship_creation(self):
        self.assertEqual(self.friend.user1.username, "user1")
        self.assertEqual(self.friend.user2.username, "user2")

