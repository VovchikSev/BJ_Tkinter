from unittest import TestCase, main
from src.game import Game


class GameTest(TestCase):
    def test_cteate_game(self):
        game = Game()
        self.assertIsInstance(game, Game)


if __name__ == '__main__':
    main()
