import unittest, pprint
from solver import sudoku

class TestSolver(unittest.TestCase):
  def test_sudoku(self):
    pp = pprint.PrettyPrinter(indent=4)

    board = [
      [3, 0, 6, 5, 0, 8, 4, 9, 0],
      [5, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 7, 0, 0, 0, 0, 3, 1],
      [0, 0, 3, 0, 1, 0, 0, 8, 0],
      [9, 0, 0, 8, 6, 3, 0, 0, 5],
      [0, 5, 0, 0, 9, 0, 6, 0, 0],
      [1, 3, 0, 0, 0, 0, 2, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    solved = sudoku(board, 9, 9)

    pp.pprint(board)
    self.assertTrue(solved)

if __name__ == "__main__":
    unittest.main()
