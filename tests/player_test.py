from unittest import TestCase, main
from src.player import *


class PlayerTest(TestCase):
    def test_cteate_Player(self):
        player = Hand('PlayerName')
        self.assertIsInstance(player, Hand)


if __name__ == '__main__':
    main()
