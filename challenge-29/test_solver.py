import unittest
from solver import flood_fill

class TestSolver(unittest.TestCase):
  def test_flood_fill_simple(self):
    self.assertEqual(flood_fill([[1,2,1]]    , 1, 3, 0, 1, 3), [[1,3,1]]    )
    self.assertEqual(flood_fill([[2,2,2]]    , 1, 3, 0, 1, 3), [[3,3,3]]    )
    self.assertEqual(flood_fill([[1],[2],[1]], 3, 1, 1, 0, 3), [[1],[3],[1]])
    self.assertEqual(flood_fill([[2],[2],[2]], 3, 1, 1, 0, 3), [[3],[3],[3]])

  #@unittest.skip("")
  def test_flood_fill_complete(self):
    lines, columns, x, y, k = 8, 8, 4, 4, 3
    screen = [
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 1, 0, 1, 1],
      [1, 2, 2, 2, 2, 0, 1, 0],
      [1, 1, 1, 2, 2, 0, 1, 0],
      [1, 1, 1, 2, 2, 2, 2, 0],
      [1, 1, 1, 1, 1, 2, 1, 1],
      [1, 1, 1, 1, 1, 2, 2, 1]
    ]
    expected_output = [
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 1, 0, 1, 1], 
      [1, 3, 3, 3, 3, 0, 1, 0],
      [1, 1, 1, 3, 3, 0, 1, 0],
      [1, 1, 1, 3, 3, 3, 3, 0],
      [1, 1, 1, 1, 1, 3, 1, 1],
      [1, 1, 1, 1, 1, 3, 3, 1]
    ]

    self.assertEqual(flood_fill(screen, lines, columns, x, y, k), expected_output)

if __name__ == "__main__":
    unittest.main()
