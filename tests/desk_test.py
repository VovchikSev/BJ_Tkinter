from unittest import TestCase, main
from src.desk import *


class DeskTest(TestCase):
    def test_cteate_Desk(self):
        desk = Desk()
        self.assertIsInstance(desk, Desk)


if __name__ == '__main__':
    main()
