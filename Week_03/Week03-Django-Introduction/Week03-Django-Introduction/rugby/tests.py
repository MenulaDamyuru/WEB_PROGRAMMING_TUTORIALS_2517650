from django.test import TestCase

from .models import Player, Position


class RugbyModelTests(TestCase):
    def test_player_can_play_several_positions(self):
        hooker = Position.objects.create(name="Hooker", specialist=True)
        prop = Position.objects.create(name="Tight Head Prop", specialist=True)
        player = Player.objects.create(firstName="Dan", lastName="Cole", squadNumber=3)
        player.positions.add(hooker, prop)
        self.assertEqual(player.positions.count(), 2)
        self.assertTrue(Position.objects.get(name="Hooker").specialist)

    def test_str(self):
        player = Player.objects.create(firstName="Dan", lastName="Cole", squadNumber=3)
        self.assertEqual(str(player), "#3 Dan Cole")
