import unittest, random
from solver import count_islands

class TestSolver(unittest.TestCase):
  def test_count_islands(self):
    grid = [
      [1,0,0,0,1],
      [1,1,0,0,0],
      [1,0,1,1,0],
      [0,0,0,0,0]
    ]
    self.assertEqual(count_islands(grid), 3)

    grid = [
      [1,0,0,0,1],
      [1,1,0,1,1],
      [1,1,0,1,1],
      [1,0,0,0,1]
    ]
    self.assertEqual(count_islands(grid), 2)

    grid = [
      [1,0,0,0,1],
      [0,1,0,1,0],
      [0,1,0,1,0],
      [1,0,0,0,1]
    ]
    self.assertEqual(count_islands(grid), 6)

    grid = [
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,1,1,1,0],
      [0,0,0,0,0]
    ]
    self.assertEqual(count_islands(grid), 1)

    grid = [
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
    ]
    self.assertEqual(count_islands(grid), 0)

    grid = [
      [1,1,1,1,1],
      [1,1,1,1,1],
      [1,1,1,1,1],
      [1,1,1,1,1]
    ]
    self.assertEqual(count_islands(grid), 1)

if __name__ == "__main__":
    unittest.main()
