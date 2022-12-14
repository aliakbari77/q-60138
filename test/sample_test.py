import unittest
import sys
sys.path.append('../Initial_project')
from solution import Piece, Board


class Test(unittest.TestCase):

	def test_add_piece(self):
		board = Board()
		piece = Piece("P", "white", (1, 1))
		board.add(piece)
		self.assertTrue((1, 1) in board.position)


if __name__ == '__main__':
    unittest.main()