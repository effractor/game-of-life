import unittest
import life


class TestCell(unittest.TestCase):
    def setUp(self):
        self.board = set([(5, 5)])
        self.life = life.Life((10, 10), self.board)

    def test_creation(self):
        self.assertEqual(self.board, self.life.get_board())

    def test_evaluation(self):
        self.life.evaluate()
        self.assertEqual(set(), self.life.get_board())


class TestBlinker(unittest.TestCase):
    def setUp(self):
        self.board = set([(5, 5), (5, 6), (5, 7)])
        self.life = life.Life((10, 10), self.board)

    def test_period1(self):
        self.life.evaluate()
        self.assertEqual(set([(4, 6), (5, 6), (6, 6)]), self.life.get_board())

    def test_period2(self):
        self.life.evaluate()
        self.life.evaluate()
        self.assertEqual(self.board, self.life.get_board())


class TestBorderX(unittest.TestCase):
    def setUp(self):
        self.board = set([(0, 0), (0, 1), (0, 2)])
        self.life = life.Life((5, 5), self.board)

    def test_period1(self):
        self.life.evaluate()
        self.assertEqual(set([(4, 1), (0, 1), (1, 1)]), self.life.get_board())


class TestBorderY(unittest.TestCase):
    def setUp(self):
        self.board = set([(0, 0), (1, 0), (2, 0)])
        self.life = life.Life((5, 5), self.board)

    def test_period1(self):
        self.life.evaluate()
        self.assertEqual(set([(1, 4), (1, 0), (1, 1)]), self.life.get_board())


if __name__ == '__main__':
    unittest.main()
